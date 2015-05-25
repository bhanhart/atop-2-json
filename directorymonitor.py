'''
Created on May 25, 2015

@author: hsd
'''

import logging
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(object):
    def __init__(self):
        pass

    def process_file(self, file_path):
        pass

class DirectoryChangedHandler(FileSystemEventHandler):

    def __init__(self, file_handler, logger):
        super(DirectoryChangedHandler, self).__init__()
        self._logger = logger or logging.getLogger(__name__)
        self._file_handler = file_handler

    def on_modified(self, event):
        if event.is_directory:
            return
        self._logger.info("File changed:" + event.src_path)
        self._file_handler.process_file(event.src_path)

class DirectoryMonitor(object):

    def __init__(self, monitored_directory, file_handler, logger):
        self._logger = logger or logging.getLogger(__name__)
        self._event_handler = \
            DirectoryChangedHandler(file_handler, self._logger)
        self._observer = Observer()
        self._observer.schedule(self._event_handler, monitored_directory)

    def run(self):
        self._observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()
        self._observer.join()

