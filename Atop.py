
import sys
import logging

import AtopCommandLine
import AtopFileParser

def main(argv=None):
    if argv is None:
        argv = sys.argv

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("AtopFileParser")

    command_line = AtopCommandLine.AtopCommandLine(argv)

    logger.debug("Atop parsing started")
    try:
        parser = AtopFileParser.AtopFileParser(logger)
        parser.parse(command_line.getFileName())
    except IOError:
        logger.error("File not found exception")
        return 1
    logger.debug("Atop parsing finished")
    return 0

if __name__ == "__main__":
    sys.exit(main())
