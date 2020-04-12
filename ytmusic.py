#!/usr/bin/python3

import os
import youtube_dl
import argparse
import prettytable
from colorama import init, Fore, Style
import re
import requests
from sys import exit


def arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "Song_Name", help="Name of the song to search", type=str, nargs="*")
    parser.add_argument(
        "-o", "--options",
        help="Display options to choose from",
        action="store_true")
    parser.add_argument(
        "-a", "--autoplay",
        help="Start playing similar songs after the requested song",
        action="store_true")
    parser.add_argument(
        "-d", "--download",
        help="Download the song instead of playing it.\
        Be careful while passing this with -a as it can\
        cause a large number of downloads",
        action="store_true")
    parser.add_argument(
        "-v", "--verbose",
        help="Verbose output",
        action="store_true")

    args = parser.parse_args()

    return args


def my_hook(d):
    if d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        global filename
        filename = file_tuple[1]
        print("\nDone downloading {}".format(file_tuple[1]))
    if d['status'] == 'downloading':
        print(f"Downloading : {d['_percent_str']}  Time Remaining : {d['_eta_str']}", end="\r")


def duration_format(duration):
    return "{0:0=2d}".format(duration // 60) + " m  " +\
        "{0:0=2d}".format(duration % 60) + " s"


played_ids = []


def next_url(url):
    data = requests.get(url)
    ids = re.findall(r"\/watch\?v=.{11}", data.text)

    ids = list(set(ids))

    for id in ids:
        if id not in played_ids:
            played_ids.append(id)
            return "https://www.youtube.com" + id


def main(args):

    ydl_opts = {'outtmpl': '%(title)s.%(ext)s',
                'quiet': not args.verbose,
                'format': '140',
                'writethumbnail': True,
                'verbose': False,
                'postprocessors': [{'key': 'FFmpegMetadata'}],
                'progress_hooks': [my_hook]}

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    if not args.Song_Name:
        print("Song name is required!!! Run ytmusic --help for help.")
        exit(-1)

    if (len(args.Song_Name) > 1):
        song_name = ' '.join(args.Song_Name)
    else:
        song_name = args.Song_Name[0]

    init()

    print(("\nSearching {}{}'" + song_name +
           "'{} on YouTube...\n").format(Style.BRIGHT,
                                         Fore.CYAN, Style.RESET_ALL))

    with ydl:
        try:
            if args.options:
                result = ydl.extract_info(
                    "ytsearch5:" + song_name, download=False)
            else:
                result = ydl.extract_info(
                    "ytsearch:" + song_name, download=False)
        except Exception as e:
            print("\nSomething is wrong.",
                  "Try checking your internet connection.\n [EXCEPTION]", e)
            exit(1)

    if 'entries' in result:
        if not args.options:
            print(("{}{}" + result['entries'][0]['title'] +
                   "{}\n").format(Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL))
        else:
            table = prettytable.PrettyTable()
            table.hrules = prettytable.HEADER
            table.vrules = prettytable.NONE
            table.field_names = ['S.No', 'Duration', 'Title']
            table.field_names = [('{}{}' + field_name + '{}').format(
                Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL)
                for field_name in table.field_names]
            table.align = "l"
            table.right_padding_width = 5
            for i in range(0, 5):
                table.add_row([i + 1, duration_format(result['entries']
                                                      [i]['duration']),
                               result['entries'][i]['title']])
            print(table)
    else:
        print("That didn't work. Try something else..\n")
        exit(0)

    index = 0

    while (args.options):
        try:
            index = int(input("\nEnter the song number (default:1) : ")) - 1
        except ValueError:
            pass
        print("\n")
        if index == -1:
            print("\nExiting")
            exit(0)
        elif (index <= i and index >= 0):
            break
        else:
            print ("Wrong Input ! Try Again..")

    url = result['entries'][index]['webpage_url']
    played_ids.append("/watch?v=" + result['entries'][index]['id'])

    while True:
        if (args.download):
            ydl.download([url])
            os.system('AtomicParsley "' + filename + '" --artwork "' + filename.replace(filename.split('.')[-1], "jpg") + '" -o tmp.m4a')
            os.remove(filename)
            os.remove(filename.replace(filename.split('.')[-1], "jpg"))
            os.rename("tmp.m4a", filename)
            print("\nDownload complete.\n")

        else:
            os.system("mpv --no-video " + url)
            print("\n")

        if args.autoplay:
            url = next_url(url)
            result = ydl.extract_info(url, download=False)
            print(("{}{}Title:{} " + result['title'] + "\n").format(
                Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL))
        else:
            break


if __name__ == "__main__":
    try:
        main(arguments())
    except KeyboardInterrupt:
        print("\nExiting\n")
