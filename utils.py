import sys
import os
import argparse
import mimetypes

def scan_file_types(directory):
    """
    Get all unique file types in directory
    directory (str): directory to scan

    return: extensions - list (str) of file extentions
    """
    extensions = []

    extensions = set()

    for root, dirs, files in os.walk(directory) :
        for file in files: 
            pathname, exten = os.path.splitext(file) 
            extensions.add(exten)

    print(extensions)

    return extensions


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory",
        type=str
    )

    args = parser.parse_args()

    directory = args.directory

    os.chdir('/')
    
    extensions = scan_file_types(directory=directory)

    



