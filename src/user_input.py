import argparse
from datetime import datetime
import sys
sys.path.append('src')
from commands import AddEntryCommand, QueryEntriesCommand, ReportCommand, PriorityCommand

class UserInputHandler:
    date_format = '%Y/%m/%d'
    time_format = '%I:%M%p'

    def parse_entry(self, subparser):
        subparser.add_argument('date', help='Date in format YYYY/MM/DD')
        subparser.add_argument('start_time', help='Time started in format HH:MM AM/PM')
        subparser.add_argument('end_time', help='Time ended in format HH:MM AM/PM')
        subparser.add_argument('task', help='Task completed')
        subparser.add_argument('tag', help='Tag for the task in :TAG format')

    def parse_query(self, subparser):
        subparser.add_argument('query_arg', help='Query argument')

    def parse_report(self, subparser):
        subparser.add_argument('start_date', help='Start date of report query range')
        subparser.add_argument('end_date', help='End date of report query range')

    def parse_priority(self, subparser):
        return None

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Time Tracker CLI App")
        subparsers = parser.add_subparsers(dest='command', help='Desired command to execute')

        entry_parser = subparsers.add_parser('record', help='Record an entry')
        self.parse_entry(entry_parser)

        query_parser = subparsers.add_parser('query', help='Query entries of a specific date, task, or tag')
        self.parse_query(query_parser)

        report_parser = subparsers.add_parser('report', help="Get report of tasks completed between two dates")
        self.parse_report(report_parser)

        priority_parser = subparsers.add_parser('priority', help="Get priority list of all tasks")
        self.parse_priority(priority_parser)

        return parser.parse_args()
    
    def _parse_date(self, date_str):
        if date_str.lower() == 'today':
            return datetime.now()
        else:
            try:
                return datetime.strptime(date_str, self.date_format)
            except ValueError:
                return None
            
    def _parse_time(self, time_str):
        time_str = time_str.upper()
        try:
            if 'AM' not in time_str and 'PM' not in time_str:
                time_str = time_str + "AM"
            return datetime.strptime(time_str, self.time_format)
        except ValueError:
            return None


    def run(self):
        args = self.parse_args()

        if args.command == 'record':
            if self._parse_date(args.date) and self._parse_time(args.start_time) and self._parse_time(args.end_time):
                date_str = self._parse_date(args.date).strftime(self.date_format)
                formatted_start_time = self._parse_time(args.start_time)
                formatted_end_time = self._parse_time(args.end_time)

                hours_spent = (formatted_end_time - formatted_start_time).total_seconds() / 3600

                start_time_str = formatted_start_time.strftime(self.time_format)
                end_time_str = formatted_end_time.strftime(self.time_format)

                command = AddEntryCommand(
                    date_str,
                    start_time_str,
                    end_time_str,
                    args.task,
                    args.tag,
                    hours_spent
                )
                res = command.execute()
                print(res)
            else:
                print("Error: Incorrect date or time format. Input date in format YYYY/mm/dd, 'today', and time in format HH:MMAM/PM (AM by default if not specified)")
                
        elif args.command == 'query':
            if '/' in args.query_arg or args.query_arg == 'today':
                command = QueryEntriesCommand(date=args.query_arg)
            elif ':' in args.query_arg:
                command = QueryEntriesCommand(tag=args.query_arg)
            else:
                command = QueryEntriesCommand(task=args.query_arg)
        
            res = command.execute()

            if res is not None:
                print(f"Query Results for \"{args.query_arg}\"")
                print("_____________")
                for entry in res:
                    for i in range(len(entry)):
                        print(entry[i], end=' ')
                    print()
            else:
                print(f'No entries found for {args.query_arg}')

        elif args.command == 'report':
            command = ReportCommand(args.start_date, args.end_date)
            res = command.execute()

            if res is not None:
                print(f"Report of activities between {args.start_date} and {args.end_date}")
                print("__________________________________________________________")
                for entry in res:
                    for i in range(1, len(entry)):
                        print(entry[i], end=' ')
                    print()
            else:
                print(f"No results for activities between {args.start_date} and {args.end_date}")

        elif args.command == 'priority':
            command = PriorityCommand()
            res = command.execute()

            if res is not None:
                print("Priority List")
                print("______________")
                
                for task, total_hours in res:
                    print(f"{task}: {total_hours} Total Hours")