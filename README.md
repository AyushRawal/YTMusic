# YTMusic

A simple python script to play songs from YouTube in terminal. Supports auto-play. A kind of YouTube music in the terminal.

## Installation

*Note: This is a python 3 script.*

Install all the dependencies

`pip3 install youtube-dl argparse prettytable colorama`

You also need to have `mpv`, `ffmpeg` and `AtomicParsley` installed.
Windows users can keep the executables in the same folder.

*Note: You will also like to have your keybindings set for mpv (if you don't like the default).
For that linux users should edit ~/.config/mpv/input.conf (create it if you don't have one) (default file can be found at /usr/share/doc/mpv/mplayer-input.conf for Ubuntu users.).
Windows users need to create input.conf in the same folder as the executable.*

## Usage

```man
usage: ytmusic [-h] [-o] [-a] [-d] [-v] [Song_Name [Song_Name ...]]

positional arguments:
  Song_Name       Name of the song to search

optional arguments:
  -h, --help      show this help message and exit
  -o, --options   Display options to choose from
  -a, --autoplay  Start playing similar songs after the requested song
  -d, --download  Download the song instead of playing it. Be careful while
                  passing this with -a as it can cause a large number of
                  downloads
  -v, --verbose   Verbose output
```

For example :

`python3 ytmusic.py -a shape of you`
