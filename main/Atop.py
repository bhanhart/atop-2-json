
import sys
import logging

from atop import AtopCommandLine, AtopFileParser

def main(argv=None):
    if argv is None:
        argv = sys.argv

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("AtopFileParser")
    
    commandLine = AtopCommandLine.AtopCommandLine(argv)
            
    logger.debug("Atop parsing started")
    try:
        parser = AtopFileParser.AtopFileParser(logger)
        parser.parse(commandLine.getFileName())
    except IOError:
        logger.error("File not found exception")
        return 1
    logger.debug("Atop parsing finished")
    return 0

if __name__ == "__main__":
    sys.exit( main() )
