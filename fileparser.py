import logging

from atoprecord import AtopRecord

class AtopFileParser(object):
    def __init__(self, logger):
        self.logger = logger or logging.getLogger(__name__)
        self.current_record = None
        self.records = []

    def parse(self, atopFileName):
        self.logger.debug("Processing file '" + atopFileName + "'")

        with open(atopFileName, 'r') as atopFile:
            self._load(atopFile)

    def _create_new_record(self, recordNo):
        self.logger.debug("Creating record " + str(recordNo))
        self.current_record = AtopRecord(recordNo)

    def _store_record(self):
        self.records.append(self.current_record)
        self.current_record = None

    def _load(self, atopFile):
        processing_totals_since_boot = False
        record_no = 0
        for line in atopFile:
            line = line.rstrip()
            if line == "RESET":
                processing_totals_since_boot = True
            elif line == "SEP":
                record_no += 1
                if processing_totals_since_boot:
                    processing_totals_since_boot = False
                else:
                    self._store_record()
                self._create_new_record(record_no)
            else:
                if processing_totals_since_boot:
                    continue
                self.current_record.parse_line(line)

        self._save_to_json_file()

    def _save_to_json_file(self):
        with open("/home/hsd/work/atop.mem.json", 'w') as json_file:
            for record in self.records:
                json_file.write(record.to_json())
                json_file.write("\n")
