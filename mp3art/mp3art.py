import argparse
from pathlib import Path


def validate_path(path):
    return True


def add_cover(args):
    mp3_path = args.mp3
    cover_path = args.cover
    print(mp3_path, cover_path)
    # print("adding cover %s to %s".format(cover_path, mp3_path))


def remove_cover(args):
    mp3_path = args.mp3
    print(mp3_path)
    # print("removing cover from %s".format(mp3_path))


def run():
    parser = argparse.ArgumentParser(prog="mp3art",
                                     description="Add or remove cover art to MP3 files.")

    subparsers = parser.add_subparsers(title="Subcommands",
                                       description="Which operation to perform.",
                                       help="Add or remove cover art for an MP3 file.",
                                       required=True)

    add_parser = subparsers.add_parser("add", help="Add cover art to an MP3 file.")
    add_parser.add_argument("mp3", type=Path, help="Path to the MP3 file.")
    add_parser.add_argument("cover", type=Path, help="Path to the cover art file.")
    add_parser.set_defaults(func=add_cover)

    remove_parser = subparsers.add_parser("remove", help="Remove cover art to an MP3 file.")
    remove_parser.add_argument("mp3", type=Path, help="Path to the MP3 file.")
    remove_parser.set_defaults(func=remove_cover)

    args = parser.parse_args()
    args.func(args)