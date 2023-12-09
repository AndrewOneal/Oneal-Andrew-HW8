import argparse
from datetime import datetime

db = []

class Command(object):
    date_format = '%Y/%m/%d'
    def execute(self): pass

class AddEntryCommand(Command):

    def __init__(self, date_str, start_time, end_time, task, tag):
        self.date = self._parse_date(date_str)
        self.start_time = start_time
        self.end_time = end_time
        self.task = task
        self.tag = tag

    def execute(self):
        db.append([self.date, self.start_time, self.end_time, self.task, self.tag])
        return "Entry added!"
    
    def _parse_date(self, date_str):
        if date_str == 'today':
            return datetime.now().strftime(self.date_format)
        else: 
            return date_str

class QueryEntriesCommand(Command):

    def __init__(self, date=None, task=None, tag=None):
        self.date = date
        self.task = task
        self.tag = tag

    def execute(self):
        if self.date:
            if self.date == 'today':
                return self._find_arg(datetime.now().strftime(self.date_format), 0)
            else:
                return self._find_arg(self.time, 1)
        if self.task:
            return self._find_arg(self.task, 3)
        if self.tag:
            return self._find_arg(self.tag, 4)


    def _find_arg(self, query_arg, query_index):
        found_entries = []
        for entry in db:
            if entry[query_index] == query_arg:
                found_entries += entry

        return found_entries

def parse_entry(subparser):
    subparser.add_argument('date', help='Date in format YYYY/MM/DD')
    subparser.add_argument('start_time', help='Time started in format HH:MM AM/PM')
    subparser.add_argument('end_time', help='Time ended in format HH:MM AM/PM')
    subparser.add_argument('task', help='Task completed')
    subparser.add_argument('tag', help='Tag for the task in :TAG format')

def parse_query(subparser):
    subparser.add_argument('query_args', help='Query argument')

def parse_args():
    parser = argparse.ArgumentParser(description="Time Tracker CLI App")
    subparsers = parser.add_subparsers(dest='command', help='Desired command to execute')

    entry_parser = subparsers.add_parser('record', help='Record an entry')
    parse_entry(entry_parser)

    query_parser = subparsers.add_parser('query', help='Query entries of a specific date, task, or tag')
    parse_query(query_parser)

    return parser.parse_args()

def main():

    while True:
        args = input()
        args = args.split()

        command = args[0]

        if command == 'record':
            command = AddEntryCommand(args[1], args[2], args[3], args[4], args[5])
            res = command.execute()
            print(res)
        elif command == 'query':
            if '/' in args[1] or args[1] == 'today':
                command = QueryEntriesCommand(date=args[1])
            elif ':' in args[1]:
                command = QueryEntriesCommand(tag=args[1])
            else:
                command = QueryEntriesCommand(task=args[1])
        
            res = command.execute()

            if res is not None:
                print(res)
                print(f"Query Results for \"{args[1]}\"")
                print("_____________")
                for entry in res:
                    print(entry)
            else:
                print(f'No entries found for {args[1]}')

if __name__ == '__main__':
    main()