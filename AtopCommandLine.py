import argparse

class AtopCommandLine(object):


    def __init__(self, argv):
        if (len(argv) <= 1):
            raise ValueError('No arguments provided')

        parser = argparse.ArgumentParser(
                                description="Convert atop files to JSON")
        parser.add_argument(
                        '--file',
                        action="store",
                        dest="atopFileName",
                        help="atop file to converted to JSON")

        self.fileName = parser.parse_args(argv[1:]).atopFileName

    def getFileName(self):
        return self.fileName

