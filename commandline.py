import argparse

class CommandLine(object):


    def __init__(self, argv):
        if (len(argv) <= 1):
            raise ValueError('No arguments provided')

        parser = argparse.ArgumentParser(
                                description="Convert atop files to JSON")
        parser.add_argument(
                        '--file',
                        required=True,
                        action="store",
                        dest="atop_file_name",
                        help="atop file to converted to JSON")
        parser.add_argument(
                        '--dir',
                        required=True,
                        action="store",
                        dest="dir_name",
                        help="directory to be monitored for atop files")

        parseResults = parser.parse_args(argv[1:])

        self._atop_file_name = parseResults.atop_file_name
        self._monitored_directory = parseResults.dir_name

    def get_atop_filename(self):
        return self._atop_file_name

    def get_monitored_directory(self):
        return self._monitored_directory


