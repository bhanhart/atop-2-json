'''
Created on May 25, 2015

@author: hsd
'''
import logging
import subprocess

from directorymonitor import FileHandler

class AtopConvertor(FileHandler):

    def __init__(self, executable, logger):
        super(AtopConvertor, self).__init__()
        self._logger = logger or logging.getLogger(__name__)
        self._executable = executable

    def process_file(self, file_path):
        self._logger.info("Executing: " + self._executable + " on " + file_path)
        subprocess.check_call(self._executable)
