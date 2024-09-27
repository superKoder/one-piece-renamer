#!/usr/bin/env python3
import argparse
import sys
import pathlib
import re
import os

from typing import List

RE_PART_EPISODE_STYLE_S99E99 = r"S\d+E\d+"
RE_PART_EPISODE_STYLE_999 = r"\d+"

# Real world examples:
#   One Piece - 711 - The Man's Pride! Bellamy's Last Charge! (1080p FUNI WEB-DL -KS-).mkv
#   One Piece S16e20 Shocking! The True Identity Of The Mystery Man Vergo!.mkv
#   One Piece S04E13 Through the Sky They Soar! The 1000 Year Legend Lives Again!.mkv
RE_EPISODE_FILENAME = r"(one.piece).*?[\s\.](" + RE_PART_EPISODE_STYLE_999 + \
    "|" + RE_PART_EPISODE_STYLE_S99E99 + r")(.*\.\w+)"

REPC_EPISODE_STYLE_S99E99 = re.compile(
    r"^" + RE_PART_EPISODE_STYLE_S99E99 + r"$", re.IGNORECASE)
REPC_EPISODE_FILENAME = re.compile(
    r"^" + RE_EPISODE_FILENAME + r"$", re.IGNORECASE)

# Require Python 3.2+
MIN_PYTHON = (3, 2)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

UNIFORM_PREFIX = "One Piece "

# Source: https://thetvdb.com/series/one-piece#seasons
EPISODES_PER_SEASON = [
    0,      # Season  0
    8,      # Season  1
    22,     # Season  2
    17,     # Season  3
    13,     # Season  4
    9,      # Season  5
    22,     # Season  6
    39,     # Season  7
    13,     # Season  8
    52,     # Season  9
    31,     # Season 10
    99,     # Season 11
    56,     # Season 12
    100,    # Season 13
    35,     # Season 14
    62,     # Season 15
    49,     # Season 16
    118,    # Season 17
    33,     # Season 18
    98,     # Season 19
    14,     # Season 20
    194,    # Season 21
    35,     # Season 22
]


def log_error(msg: str):
    sys.stderr.write("-error: %s\n" % msg)

def log_info(msg: str):
    sys.stdout.write("+info: %s\n" % msg)


def is_episode_style(style, episode: str) -> bool:
    """
    Returns True if `episode` matches `style`. 
    """
    if style.match(episode):
        return True
    return False


def is_already_good_style(episode: str) -> bool:
    """
    Returns True on a "S03E12" style. 
    """
    return is_episode_style(REPC_EPISODE_STYLE_S99E99, episode)


def convert_episode(episode: int) -> str:
    """
    Looks up the `S03E12` style notation for the Nth episode
    """
    season = 1
    while episode > EPISODES_PER_SEASON[season]:
        episode -= EPISODES_PER_SEASON[season]
        season += 1
    return f"S%02dE%02d" % (season, episode)


def convert_filename(filename: str) -> str:
    """
    The main logic of converting `One Piece - 600 BlaBla.mkv` into `One Piece S16E22 BlaBla.mkv`.
    """
    matches = REPC_EPISODE_FILENAME.match(filename)
    if not matches:
        log_error(f"Does not match: %s" % filename)
        return filename
    _ = matches.group(1)
    episode = matches.group(2)
    suffix = matches.group(3)
    if not is_already_good_style(episode):
        episode = convert_episode(int(episode))
    return UNIFORM_PREFIX + episode + suffix


def convert_path(path: pathlib.PosixPath) -> pathlib.PosixPath:
    """
    Calls `convert_filename` on the filename, and re-prepends it with the original location.
    """
    location = path.parent
    filename = path.name
    return pathlib.PosixPath(location, convert_filename(filename))


def resolve_all_or_fail(paths: List[pathlib.PosixPath]):
    """
    Turns the list of relative paths (passed on the command line) to a list of absolute paths, resolving 
    things like softlinks and home dirs.
    """
    resolved_paths: List[pathlib.PosixPath] = list()
    has_unresolved = False
    for path in paths:
        resolved_path = path.resolve()
        if not resolved_path.exists():
            has_unresolved = True
            log_error("File not found: %s" % path)
        resolved_paths.append(resolved_path)
    if has_unresolved:
        return []
    return resolved_paths


def rename_if_needed(path: pathlib.PosixPath):
    """
    Does the actual renaming of the file.
    """
    converted_path = convert_path(path)
    if converted_path == path:
        log_info(f"skipping '%s'" % path)
        return
    log_info(f"RENAMING '%s' to '%s'" % (path, converted_path))
    os.rename(path, converted_path)


def main():
    parser = argparse.ArgumentParser(
        prog="one-piece-rename",
        description="Renames filenames by converting the episode number of One Piece episodes",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=pathlib.Path,
        metavar="filename",
    )
    args = parser.parse_args()

    for path in resolve_all_or_fail(args.paths):
        rename_if_needed(path)

if __name__ == "__main__":
    main()
