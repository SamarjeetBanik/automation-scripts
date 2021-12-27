from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

class move_file_Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for each_file in os.listdir(main_folder):
            src = main_folder + "/" + each_file
            destination = destination_folder + "/" + each_file
            os.rename(src, destination)

main_folder = "/Users/ASUS/Downloads"
destination_folder = "/Users/ASUS/Documents/New folder"

event_handler = move_file_Handler()
observer = Observer()

observer.schedule(event_handler, main_folder, recursive=True)
observer.start()

try:
    while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()