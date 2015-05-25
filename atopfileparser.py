import logging

from atopsample import AtopSample

class AtopFileParser(object):
    def __init__(self, logger):
        self._logger = logger or logging.getLogger(__name__)
        self.current_record = None
        self.samples = []

    def parse(self, atop_filename):
        self._logger.debug("Processing file '" + atop_filename + "'")

        with open(atop_filename, 'r') as atop_file:
            self._load(atop_file)

    def _create_new_sample(self, sample_no):
        self.current_record = AtopSample(sample_no, self._logger)

    def _store_sample(self):
        self.samples.append(self.current_record)
        self.current_record = None

    def _load(self, atop_file):
        processing_totals_since_boot = False
        sample_no = 0
        for line in atop_file:
            line = line.rstrip()
            if line == "RESET":
                processing_totals_since_boot = True
            elif line == "SEP":
                sample_no += 1
                if processing_totals_since_boot:
                    processing_totals_since_boot = False
                else:
                    self._store_sample()
                self._create_new_sample(sample_no)
            else:
                if processing_totals_since_boot:
                    continue
                self.current_record.parse_line(line)

        self._save_to_json_file()

    def _save_to_json_file(self):
        with open("/home/hsd/work/atop.mem.json", 'w') as json_file:
            for sample in self.samples:
                json_file.write(sample.to_json())
                json_file.write("\n")
