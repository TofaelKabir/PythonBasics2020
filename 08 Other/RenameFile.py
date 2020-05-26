import os
import shutil
from os import path


def main():
    # make a duplicate of an existing file
    if path.exists("test.txt"):
        # get the path to the file in the current directory
        src = path.realpath("test.txt")

    # rename the original file
    os.rename('test.txt', 'pythonTest.txt')


if __name__ == "__main__":
    main()
