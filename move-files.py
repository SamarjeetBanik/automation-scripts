# `pip install watchdog` for below mentioned package to work!
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# https://pypi.org/project/watchdog/ <- visit here to know more about "watchdog".

# in-built standard utility modules
import os
import time 

# event handler class to fetch the files from the mentioned paths
class move_file_Handler(FileSystemEventHandler):
    def on_modified(self, event): # Called when a file or directory is modified.
        for each_file in os.listdir(main_folder):
            src = main_folder + "/" + each_file
            destination = destination_folder + "/" + each_file
            os.rename(src, destination)

# paths (from "main_folder" to "destination_folder")
main_folder = "/Users/ASUS/Downloads"
destination_folder = "/Users/ASUS/Documents/New folder"

# object instantiation
event_handler = move_file_Handler()
observer = Observer()

observer.schedule(event_handler, main_folder, recursive=True) # 
observer.start() # folder activity lookup/monitoring starts

try:
    while True:
        # debugging
        # time_stamp = time.localtime()
        # parsed_time_stamp = time.strftime("%I:%M:%S %p", time_stamp)
        # print(parsed_time_stamp)

        # pause time of 1 sec
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop() # on interruption from keyboard (ctrl + c), the the program execution stops

observer.join() # Wait until the thread terminates.