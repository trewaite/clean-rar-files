#!/bin/sh

echo Directory from Root:
read direc

echo List of file extensions to delete:
read del_extensions 

echo Type of file to keep:
read keep_str

python3 rar_clean.py --directory $direc --extensions $del_extensions --keep $keep_str