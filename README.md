# Command line tool to rename **One Piece (1999)** episodes

## Why

Tools like Plex and Sonarr use "S01E05" style episode notations. Many sources, however, don't name One Piece (1999) episodes like this. Instead, they use an increasing number. You'd need to rename those in order to be recognized.

For example, if you find an episode `"One Piece - 600 - Whatever.mkv"`, it should be renamed to `"One Piece S16E22 Whatever.mkv"` so Plex, Sonarr and others will treat the file correctly.

That's a lot of manual work!! ... Until now.

## How to use

### Prep step - Do this only once

1. This is command line tool, written in Python. Unless your computer already has it, you have to [download and install Python 3](https://www.python.org/downloads/). That is the official link and it should be safe.

2. You need to download this script. Assuming you are not a software developer, the easiest way is to simply download the `one_piece_rename.py` file. You don't really need the other files. But you may need to do this again as new seasons are released in the future.

### Convert your files on Mac or Linux

For every One Piece video file you want to rename, do:

```shell
python3 path/to/one_piece_rename.py path/to/filename
```

For example, you can rename a single file as such:

```shell
python3 ./one_piece_rename.py ~/completed/One\ Piece\ -\ 600\ BlaBla.mkv
```

In reality though, you'll probably want to covert **multiple files at the same time**, right?

This would convert all files in a `Voyage 11` folder:

```shell
python3 ./one_piece_rename.py ~/completed/Voyage\ 11/*.mkv
```

Of course, you can do more complex things such as:

```shell
find /media/One\ Piece/ -type f -iname '*.mkv' -exec python3 ./one_piece_rename.py '{}' \;
```

### Convert your files on Windows

This should work just the same on Windows (provided you followed the prep steps above), but the paths are different on Windows.

Example of single file:

```shell
C:\> python3 %HOME%\Downloads\one_piece_rename.py "completed\One Piece - 600 BlaBla.mkv"
```

And this also counts for the other examples in the Linux/Mac section above.

(If you understand everything I said and you're on Windows, please contribute examples?)

## Contributing

### Non-Engineers

1. Please, make this README.md file better. Fix typos, add examples.

2. If a new season releases, someone we'll need to add it. Anyone can do that.

### Engineers

You are welcome to join this effort if you want! I will accept all improvements.

If you make any changes, make sure to run the unit tests:

```shell
$ pytest
=========================== test session starts ===========================
platform darwin -- Python 3.11.4, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/koder/prog/one-piece-renamer
collected 2 items                                                         

one_piece_rename_test.py ..                                         [100%]

============================ 2 passed in 0.00s ============================
```
