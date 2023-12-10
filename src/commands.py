import sys
sys.path.append('src')
from database import DatabaseController

class Command(object):
    def execute(self): pass

class AddEntryCommand(Command):

    def __init__(self, date_str, start_time, end_time, task, tag):
        self.date = date_str
        self.start_time = start_time
        self.end_time = end_time
        self.task = task
        self.tag = tag

    def execute(self):
        DatabaseController().addEntry(self.date, self.start_time, self.end_time, self.task, self.tag)
        return "Entry added!"

class QueryEntriesCommand(Command):

    def __init__(self, date=None, task=None, tag=None):
        self.date = date
        self.task = task
        self.tag = tag

    def execute(self):
        return DatabaseController().queryEntry(self.date, self.task, self.tag)
    
class ReportCommand(Command):
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def execute(self):
        return DatabaseController().queryReport(self.start_date, self.end_date)
