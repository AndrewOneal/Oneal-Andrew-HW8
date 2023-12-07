import argparse
import sys
sys.path.append('src')
from commands import AddEntryCommand, QueryEntriesCommand

def parse_args():
    parser = argparse.ArgumentParser(description="Time Tracker CLI App")
    parser.add_argument('command', choices=['record', 'query'], help='Desired command to execute')
    parser.add_argument('date', help='Date in format YYYY/MM/DD')
    parser.add_argument('start_time', help='Time started in format HH:MM AM/PM')
    parser.add_argument('end_time', help='Time ended in format HH:MM AM/PM')
    parser.add_argument('task', help='Task completed')
    parser.add_argument('tag', help='Tag for the task in :TAG format')

    return parser.parse_args()

def main():
    args = parse_args()

    if args.command == 'record':
        command = AddEntryCommand(args)