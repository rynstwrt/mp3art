from sys import argv


# EXAMPLES:
# mp3art --add <mp3 file> <cover art>
# mp3art --remove <mp3 file>
USAGE_MESSAGE = "Usage: mp3art (--add | --remove) <mp3 file> [cover art]"
# USAGE_MESSAGE = ("Usage:\n"
#                  "mp3art --add <mp3 file> <cover art>\n"
#                  "mp3art --remove <mp3 file>")


def print_padded(text):
    print("\n" + text + "\n")


def run():
    if len(argv) == 1 or "-h" in argv:
        print("help")
        return

    if not 3 <= len(argv) <= 4:
        print_padded("Incorrect usage!\n" + USAGE_MESSAGE)
        return


# USAGE_MESSAGE = "Usage: pwdf <file>"
#
#
# def run():
#     if len(argv) != 2:
#         print(USAGE_MESSAGE)
#         return
#
#     file_path = argv[1]
#     if not path.isfile(file_path):
#         print("ERROR: The file specified could not be found.")
#         print(USAGE_MESSAGE)
#         return
#
#     abs_path = path.abspath(file_path)
#     print(abs_path)
