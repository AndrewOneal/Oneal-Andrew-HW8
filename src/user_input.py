import argparse
import sys
sys.path.append('src')
from commands import AddEntryCommand, QueryEntriesCommand

def parse_entry(subparser):
    subparser.add_argument('date', help='Date in format YYYY/MM/DD')
    subparser.add_argument('start_time', help='Time started in format HH:MM AM/PM')
    subparser.add_argument('end_time', help='Time ended in format HH:MM AM/PM')
    subparser.add_argument('task', help='Task completed')
    subparser.add_argument('tag', help='Tag for the task in :TAG format')

def parse_query(subparser):
    subparser.add_argument('query_arg', help='Query argument')

def parse_args():
    parser = argparse.ArgumentParser(description="Time Tracker CLI App")
    subparsers = parser.add_subparsers(dest='command', help='Desired command to execute')

    entry_parser = subparsers.add_parser('record', help='Record an entry')
    parse_entry(entry_parser)

    query_parser = subparsers.add_parser('query', help='Query entries of a specific date, task, or tag')
    parse_query(query_parser)

    return parser.parse_args()

def main():
    args = parse_args()

    if args.command == 'record':
        command = AddEntryCommand(args.date, args.start_time, args.end_time, args.task, args.tag)
        res = command.execute()
        print(res)
    elif args.command == 'query':
        if '/' in args.query_arg or args.query_arg == 'today':
            command = QueryEntriesCommand(date=args.query_arg)
        elif ':' in args.query_arg:
            command = QueryEntriesCommand(tag=args.query_arg)
        else:
            command = QueryEntriesCommand(task=args.query_arg)
    
        res = command.execute()

        if res is not None:
            # make this look better
            print(f"Query Results for \"{args.query_arg}\"")
            print("_____________")
            for entry in res:
                for i in range(1, len(entry)):
                    print(entry[i], end=' ')
                print()
        else:
            print(f'No entries found for {args.query_arg}')