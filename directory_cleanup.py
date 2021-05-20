import os
from pathlib import Path
import sys,getopt,shutil

SUBDIRECTORIES = {
    "DOCUMENTS":['.pdf', '.rtf', '.txt.', '.docx'],
    "DATA": ['.xlsx', '.csv'],
    "AUDIO":['.m4a','m4b','.mp3'],
    "VIDEOS":['.mov', '.avi','.mp4'],
    "IMAGES": ['.jgp','.jpeg', '.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"



def organizeDirectory(patharg):
    for item in os.scandir(patharg):
        if item.is_dir():
            continue
        filePath = Path(item)
        print(filePath)
        filetype = filePath.suffix.lower()
        directoryPath = patharg.joinpath(Path(pickDirectory(filetype)))
        print(directoryPath)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
            print("Directory created")
        shutil.move(str(filePath), str(directoryPath))


def main(argv):
    message = 'directory_cleanup.py -h -i <filepath>'
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except:
        print(message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(message)
        elif opt in ("-i"):
            pathArg = Path(arg)
            organizeDirectory(pathArg)
            print("Cleanup successful!")

main(sys.argv[1:])