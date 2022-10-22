import sys , time , random, os, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source  = 'C:/Users/Raj'

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("A new path has been created in " + event.src_path + ".")

    def on_deleted(self, event):
        print("The path " + event.src_path + " has been deleted.")

    def on_moved(self, event):
        print("The file " + event.src_path + " has been moved.")

    def on_deleted(self, event):
        print("The file " + event.src_path + " has been deleted.")

    def on_modified(self, event):
        print("The file" + event.src_path + " was modified recently")

handler = FileEventHandler()
observer = Observer()
observer.schedule(handler,source,recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
        print("Tracking file movement...")
except KeyboardInterrupt:
    print("File tracking stopped")
    observer.stop()
    
