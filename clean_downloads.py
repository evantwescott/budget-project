import time
import os
import getopt, sys

def main(argv):
    message = 'clean_downloads.py -h -i <filepath>'
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except:
        print(message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(message)
        elif opt in ("-i"):
            cleanupAction(argv)

def cleanupAction(path):
    os.chdir(str(path))
    files = os.listdir(os.getcwd())
    present_time = time.time()
    days = 30*24*60*60

    for file_name in files:
        if not os.path.isdir(file_name):
            access_time = os.stat(file_name).st_atime
            if access_time < (present_time-days):
                os.remove(file_name)
                print(file_name + " removed")
        print("Cleanup complete!")

main(sys.argv[1:])
