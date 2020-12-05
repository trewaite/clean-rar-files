#!/bin/sh

# your video file directory
echo Directory from Root:
read direc

# ['r']
echo List of file extensions to delete:
read del_extensions 

# type 'video' for video type
echo Type of file to keep:
read keep_str

python3 rar_clean.py --directory $direc --extensions $del_extensions --keep $keep_str