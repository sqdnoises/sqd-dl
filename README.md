# PyVid Simple
![MIT license](https://img.shields.io/badge/license-MIT-brightgreen)
![Python language](https://img.shields.io/badge/language-Python-yellow)
![Trivago hotel](https://img.shields.io/badge/hotel-Trivago-orange)

Simple command line app/tool to download youtube videos easily!

## Getting Started
Clone this repository or download the zip and extract it to a folder you like.
<br>
(ℹ) This program downloads to the folder you start the program in.

### Requirements
You need [Python 3.6+](https://www.python.org/downloads/) for this to work.
<br>
This program uses the [`yt-dlp`](https://pypi.org/project/yt-dlp/) package.

### Install pip Requirements
Open a terminal in the folder this readme is in.

#### On Windows:
Make sure python is on path and pip was installed in python installation.
<br>
Run:
```
python -m pip install -r requirements.txt
```

#### On MacOS/Linux:
Make sure python3 is on path.
<br>
(If this command gives an error saying no module named pip or something, make sure any python pip related packages are installed.)
<br>
Run:
```
python3 -m pip install -r requirements.txt
```

## To run
Open a terminal in the src folder.

### On windows:
Make sure python is on path.
<br>
Run:
```
py pyvid.py
```

### On MacOS/Linux:
Make sure python3 is on path.
<br>
Run:
```
python3 pyvid.py
```

## To use
It's easy to use this.
<br>
After running it, you can either:
- download youtube video from link
- download first video from search
- exit the program

### download youtube video from link
To download a youtube video from link, just type or paste the link and press enter.
<br>
The download should start automatically if the video exists.

### download first video from search
To download first video from search, type `+` before what you want to search.
<br>
The download should start automatically after a video is found.

### exit the program
Type `exit` to exit or press `Ctrl` + `C` on your keyboard to exit.

### Examples
```py
$ python3 pyvid.py
type `exit` or press ctrl + c to exit
[0] enter youtube link to download or download first search result by +<what to search>
> https://www.youtube.com/watch?v=dQw4w9WgXcQ
your input: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
... download progress ...
[0] download for `https://www.youtube.com/watch?v=dQw4w9WgXcQ` complete

[1] enter youtube link to download or download first search result by +<what to search>
> +funeral - back2sleep (lyrics)
your input: `+funeral - back2sleep (lyrics)`
... download progress ...
[1] download for `funeral - back2sleep (lyrics)` complete

[2] enter youtube link to download or download first search result by +<what to search>
> + wenomechainsama full video
your input: `+ wenomechainsama full video`
... download progress ...
[2] download for `wenomechainsama full video` complete

[3] enter youtube link to download or download first search result by +<what to search>
> exit
your input: `exit`

exited loop

$
```