import sys
import os
import mimetypes
import argparse

def find_dir_to_clean(directory, remove_ext, file_type):
    """
    -------------
    directory: directory to scan
    remove_ext (list, str): files with this extention to be removed
    -------------
    return: None 
    """

    dir_to_clean = []

    for root, dirs, files in os.walk(directory):

        video_in_dir = False
        compressed_file_in_dir = False

        for file in files:
            if video_in_dir is False:
                try:
                    video_in_dir = mimetypes.guess_type(os.path.join(root, file))[0].startswith(file_type)
                except:
                    pass

            if any([True if ext in os.path.splitext(file)[1] else False for ext in remove_ext]):
                compressed_file_in_dir = True
            
            if video_in_dir and compressed_file_in_dir:
                dir_to_clean.append(root)
                break  

    print(f"Found {len(dir_to_clean)} unique directories to clean.")
    print(f"Example directories: {dir_to_clean[0:3]}.\n")

    return dir_to_clean


def clean_dir(dir_to_clean, remove_ext):
    """
    dir_to_clean (list, str): directories to clean
    remove_ext (list,str): extensions to delete
    ----------------
    return: None
    """
    file_size_del = 0
    files_count = 0
    for direc in dir_to_clean:
        for file in os.listdir(direc):
            if any([True if ext in os.path.splitext(file)[1] else False for ext in remove_ext]):
                files_count += 1
                file_size_del += os.path.getsize(os.path.join(direc, file))
                os.remove(os.path.join(direc, file))

    print(f"Removed {file_size_del/(1000**3)} Gb over {files_count} files and {len(dir_to_clean)} directories.")

    return None

    
if __name__ == "__main__":

    # arugments 
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory",
        type=str
    )

    parser.add_argument(
        "--extensions",
        type=list
    )

    parser.add_argument(
        "--keep",
        type=str
    )


    args = parser.parse_args()

    directory = args.directory
    compressible_file_types  = args.extensions
    file_type_to_keep  = args.keep

    # find directories to clean
    os.chdir('/')
    directories_to_clean = find_dir_to_clean(directory=directory,
                                             remove_ext=compressible_file_types,
                                             file_type=file_type_to_keep)

    clean_dir(dir_to_clean=directories_to_clean,
              remove_ext=compressible_file_types)

