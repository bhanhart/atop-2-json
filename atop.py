"""
    Parse an atop text file and convert to JSON format.
"""
import sys
import logging

from configparser import SafeConfigParser

from commandline import CommandLine
from atopfileparser import AtopFileParser
from atopconvertor import AtopConvertor
from directorymonitor import DirectoryMonitor

def main(argv=None):
    """ Read the passed in atop text file and convert to JSON """

    if argv is None:
        argv = sys.argv

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("AtopParser")

    cnf = SafeConfigParser()
    cnf.read("atop.ini")

    command_line = CommandLine(argv)

    watcher = DirectoryMonitor(
        command_line.get_monitored_directory(),
        AtopConvertor("ls", logger),
        logger)
    watcher.run()

    logger.debug("Atop parsing started")
    try:
        parser = AtopFileParser(logger)
        parser.parse(command_line.get_atop_filename())
    except IOError:
        logger.error("File not found exception")
        return 1
    logger.debug("Atop parsing finished")
    return 0

if __name__ == "__main__":
    sys.exit(main())
