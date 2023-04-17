#!/usr/bin/python3

import os
import yt_dlp as yt 
import argparse
import prettytable
from colorama import init, Fore, Style
import re
import requests
from sys import exit


def my_hook(d):
    if d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        print("\nDone downloading {}".format(file_tuple[1]))
    if d['status'] == 'downloading':
        print(f"Downloading : {d['_percent_str']}  Time Remaining : {d['_eta_str']}", end="\r")


ydl_opts = {'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'format': '140',
            'verbose': False,
            'postprocessors': [{'key': 'FFmpegMetadata'}],
            'progress_hooks': [my_hook],
            'cachedir' : False
            }

ydl = yt.YoutubeDL(ydl_opts)


played_ids = []


def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-o", "--options",
        help="Display a list of songs to choose from",
        action="store_true")
    parser.add_argument(
        "-a", "--autoplay",
        help="Start playing similar songs after the requested song or playlist",
        action="store_true")
    parser.add_argument(
        "-d", "--download",
        help="Download the song or playlist instead of playing it.\
        Be careful while passing this with -a as it can\
        cause a large number of downloads",
        action="store_true")
    parser.add_argument(
        "-u", "--url",
        help="Ask for playlist url instead of song. Play / Download songs from the given url.\
        Passing -o with it will not work.",
        action="store_true")

    args = parser.parse_args()

    return args


def duration_format(duration):
    return "{:02d}".format(int(duration // 60)) + " m  " +\
        "{:02d}".format(int(duration % 60)) + " s"


def next_url(url):
    data = requests.get(url)
    ids = re.findall(r"\/watch\?v=.{11}", data.text)

    ids = list(set(ids))

    for id in ids:
        if id not in played_ids:
            played_ids.append(id)
            return "https://www.youtube.com" + id


def download_or_play(entry, download):
    url = entry['webpage_url']
    played_ids.append("/watch?v=" + entry['id'])
    print(("\n{}{}" + entry['title'] +
        "{}\n").format(Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL))
    if (download):
        ydl.download([url])
        print("\nDownload complete.\n")
    else:
        os.system("mpv --no-video " + url)
    return(url)


def main(args):

    init()

    if (not args.url):
        song_name = input("Enter song name to search for : ")
        print(("\nSearching {}{}'" + song_name +
            "'{} on YouTube...").format(Style.BRIGHT,
                                            Fore.CYAN, Style.RESET_ALL))
        if args.options:
            search_query = "ytsearch5:" + song_name
        else:
            search_query = "ytsearch:" + song_name
    else:
        search_query = input("Enter the playlist url : ")

    try:
        result = ydl.extract_info(
                    search_query, download=False)
    except Exception as e:
        print("\nSomething is wrong.",
            "Try checking your internet connection.\n [EXCEPTION]", e)
        exit(1)

    if 'entries' in result:
        if args.options or args.url:
            print("\n")
            table = prettytable.PrettyTable()
            table.hrules = prettytable.HEADER
            table.vrules = prettytable.NONE
            table.field_names = ['S.No', 'Duration', 'Title']
            table.field_names = [('{}{}' + field_name + '{}').format(
                Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL)
                for field_name in table.field_names]
            table.align = "l"
            table.right_padding_width = 5
            for i, entry in enumerate(result['entries'], start=1):
                table.add_row([i, duration_format(entry['duration']),
                            entry['title']])
            print(table)
    else:
        print("That didn't work. Try something else..\n")
        exit(0)

    index = 0

    while (args.options and not args.url):
        try:
            index = int(input("\nEnter the song number (default:1) : ")) - 1
        except ValueError:
            pass
        if index == -1:
            print("\nExiting")
            exit(0)
        elif (index <= 5 and index >= 0):
            break
        else:
            print ("Wrong Input ! Try Again..")

    url = ""
    if not args.url:
        url = download_or_play(result['entries'][index], args.download)

    else:
        for entry in result['entries']:
            url = download_or_play(entry, args.download)

    if args.autoplay:
        while True:
            url = next_url(url)
            result = ydl.extract_info(url, download=False)
            download_or_play(result, args.download)

if __name__ == "__main__":
    try:
        main(arguments())
    except KeyboardInterrupt:
        print("\nExiting\n")
