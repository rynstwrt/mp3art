import argparse
from pathlib import Path


VALID_AUDIO_EXTENSIONS = [".mp3"]
VALID_IMAGE_EXTENSIONS = [".png"]



def validate_path(file_path: Path, is_audio_path: bool):
    path_type = "MP3" if is_audio_path else "Cover art"

    if not file_path.is_file():
        print(f'{path_type} path "{file_path}" was not found or is not a file!')
        return False

    valid_extensions = VALID_AUDIO_EXTENSIONS if is_audio_path else VALID_IMAGE_EXTENSIONS
    file_extension = file_path.suffix.lower()
    if file_extension not in valid_extensions:
        print(f'{path_type} file has invalid extension "{file_extension}"! Valid extensions: {", ".join(valid_extensions)}.')
        return False

    return True



def add_cover(args):
    mp3_path = args.mp3
    cover_path = args.cover
    print(mp3_path, cover_path)

    if not validate_path(mp3_path, True) or not validate_path(cover_path, False):
        return False

    print("AAAA")



def remove_cover(args):
    mp3_path = args.mp3
    print(mp3_path)

    if not validate_path(mp3_path, True):
        return False

    print("A")



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