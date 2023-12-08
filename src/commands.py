import sys
from datetime import datetime
sys.path.append('src')
from database import DatabaseController

class Command(object):
    date_format = '%Y/%m/%d'
    time_format = '%I:%m'
    time_format_ampm = '%I:%m%p'

    def execute(self): pass

class AddEntryCommand(Command):
    db = DatabaseController()

    def __init__(self, date_str, start_time, end_time, task, tag):
        self.date = self._parse_date(date_str)
        self.start_time = start_time
        self.end_time = end_time
        self.task = task
        self.tag = tag

    def execute(self):
        self.db.addEntry(self.date, self.start_time, self.end_time, self.task, self.tag)
        return "Entry added!"
    
    def _parse_date(self, date_str):
        if date_str == 'today':
            return datetime.now().strftime(self.date_format)
        else: 
            return date_str

class QueryEntriesCommand(Command):
    db = DatabaseController()

    def __init__(self, date=None, task=None, tag=None):
        self.date = date
        self.task = task
        self.tag = tag

    def execute(self):
        return self.db.queryEntry(self.date, self.task, self.tag)
        

