import sys
sys.path.append('src')
from database import DatabaseController

class Command(object):
    def execute(self): pass

class AddEntryCommand(Command):
    db = DatabaseController()

    def __init__(self, date, start_time, end_time, task, tag):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.task = task
        self.tag = tag

    def execute(self):
        self.db.addEntry(self.date, self.start_time, self.end_time, self.task, self.tag)

class QueryEntriesCommand(Command):
    db = DatabaseController()

    def __init__(self, date=None, task=None, tag=None):
        self.date = date
        self.task = task
        self.tag = tag

    def execute(self):
        self.db.queryEntry(self.date, self.task, self.tag)

