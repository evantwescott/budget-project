import time
import os

os.chdir(r'C:\Users\evan.wescott\Downloads')
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