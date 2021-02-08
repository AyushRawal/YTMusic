<h1 align=center>YTMusic</h1><br>

<p align=center><img src="https://img.shields.io/github/stars/AyushRawal/YTMusic?style=social"> <img src="https://img.shields.io/github/forks/AyushRawal/YTMusic?style=social"> <img src="https://img.shields.io/badge/Category-Music-blue?style=flat-square"> <img src="https://img.shields.io/badge/Category-CLI-green?style=flat-square"> <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-Welcome-green?style=flat-square"></a> <a href="https://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/License-MIT-orange?style=flat-square"></a><br><br><img src="https://img.shields.io/badge/Python 3%20-%2314354C.svg?&style=flat-square&logo=python&logoColor=white"/> <a href="https://github.com/ytdl-org/youtube-dl"><img src="https://img.shields.io/badge/Built Using-youtube--dl-yellow?style=flat-square"></a></p>



Listen to songs from your terminal !! 🎷 
A kind of YouTube music in the terminal.

YTMusic is a simple python script to play songs from YouTube in terminal.

It also supports auto-play and playlists. 😁
You can also download songs to listen to them offline.



### Demo :

![demo](demo.gif)



I had a potato computer before and opening a browser or some heavy bloated app just to listen to some music.... not good. 😓

Since I use terminal for a lot of my tasks anyway, I wrote this script to play songs from the terminal and still use it even on my new machine. It uses youtube-dl and mpv to stream and download songs. 😎



## Installation 🔨

**Clone this repository**

​	`git clone https://github.com/AyushRawal/YTMusic.git`

**Install all the python dependencies:**

​	`pip install youtube-dl argparse prettytable colorama requests`

​	You may need to replace pip with pip3 if you are using Linux and python3 is not the default.

**You also need to have `mpv` installed.**
(Windows users can keep the executables in the same folder as the script.)



*Note: You will also like to have your key-bindings set for mpv (if you don't like the default).
For that, Linux users should edit `~/.config/mpv/input.conf` (create it if you don't have one) (default file can be found at `/usr/share/doc/mpv/mplayer-input.conf` for Ubuntu users.).
Windows users need to create `input.conf` in the same folder as the executable.*



## Usage 💻

```
usage: ytmusic.py [-h] [-o] [-a] [-d] [-u]

optional arguments:
  -h, --help      show this help message and exit
  -o, --options   Display a list of songs to choose from
  -a, --autoplay  Start playing similar songs after the requested song or playlist
  -d, --download  Download the song or playlist instead of playing it. Be careful while passing this
                  with -a as it can cause a large number of downloads
  -u, --url       Ask for playlist url instead of song. Play / Download songs from the given url.
                  Passing -o with it will not work.
```



## Changelog 📋

- Now, you can play / download your playlists by providing the URL of the playlist.
- It no longer embeds album art in the downloaded songs (_at least for now_). I had to remove it since YouTube now supports multiple formats for thumbnails and AtomicParsley only supports jpg and png formats :disappointed:.
- AtomicParsley is no longer a requirement due to the above mentioned point.
- FFMpeg is also not a requirement anymore.



## Support 🙏

​	Please drop a star ⭐ if you like this project.



## Contributing

​	Please open an issue before making any major changes.



## Contact ✉

​	Ayush Rawal - [GitHub](https://github.com/AyushRawal) - E-mail : royalrawal.2001@gmail.com - [Twitter](https://twitter.com/_royal_rawal_)



_**Note :** Please feel free to ask for a feature or report any bug by opening an issue._



<p align=center>Made with ❤️ for 🌏 Everyone</p>
