"""
    Parse an atop text file and convert to JSON format.
"""
import sys
import logging

from commandline import CommandLine
from fileparser import AtopFileParser


def main(argv=None):
    """ Read the passed in atop text file and convert to JSON """

    if argv is None:
        argv = sys.argv

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("fileparser")

    command_line = CommandLine(argv)

    logger.debug("Atop parsing started")
    try:
        parser = AtopFileParser(logger)
        parser.parse(command_line.getFileName())
    except IOError:
        logger.error("File not found exception")
        return 1
    logger.debug("Atop parsing finished")
    return 0

if __name__ == "__main__":
    sys.exit(main())
