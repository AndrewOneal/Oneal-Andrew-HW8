import sys
sys.path.append('src')
from database import DatabaseController
from commands import *

def test_AddEntryCommand():
    date_str = "2023/12/10"
    start_time = "10:00"
    end_time = "12:00"
    task = "Sample Task"
    tag = "Sample Tag"
    hours_spent = 2.0

    command = AddEntryCommand(date_str, start_time, end_time, task, tag, hours_spent)
    result = command.execute()

    assert result == "Entry added!"

    entries = DatabaseController().queryAllEntries()
    assert entries is not None
    assert len(entries) == 1
    assert entries[0][1] == date_str
    assert entries[0][2] == start_time
    assert entries[0][3] == end_time
    assert entries[0][4] == task
    assert entries[0][5] == tag
    assert entries[0][6] == hours_spent

    DatabaseController().deleteAll()

def test_QueryEntriesCommand():
    start_time = "10:00PM"
    end_time = "11:00PM"
    hours_spent = 2.5

    command = AddEntryCommand("today", start_time, end_time, "task_today", ":TAGTODAY", hours_spent)
    command.execute()
    command = AddEntryCommand("2023/1/1", start_time, end_time, "task_date", ":TAGDATE", hours_spent)
    command.execute()
    command = AddEntryCommand("2023/1/2", start_time, end_time, "example task", ":TAGTASK", hours_spent)
    command.execute()
    command = AddEntryCommand("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG", hours_spent)
    command.execute()

    command = QueryEntriesCommand(date="today")
    res = command.execute()
    assert(res[0][0] == "today")
    assert(res[0][3] == "task_today")
    assert(res[0][4] == ":TAGTODAY")

    command = QueryEntriesCommand(date="2023/1/1")
    res = command.execute()
    assert(res[0][0] == "2023/1/1")
    assert(res[0][3] == "task_date")
    assert(res[0][4] == ":TAGDATE")

    command = QueryEntriesCommand(task="example task")
    res = command.execute()
    assert(res[0][0] == "2023/1/2")
    assert(res[0][3] == "example task")
    assert(res[0][4] == ":TAGTASK")
    
    command = QueryEntriesCommand(tag=":TASKTAG")
    res = command.execute()
    assert(res[0][0] == "2023/1/3")
    assert(res[0][3] == "task_tag")
    assert(res[0][4] == ":TASKTAG") 

    DatabaseController().deleteAll()


def test_ReportCommand():
    start_time = "10:00PM"
    end_time = "11:00PM"
    hours_spent = 2.5
    command = AddEntryCommand("2023/1/1", start_time, end_time, "task_today", ":TAGTODAY", hours_spent)
    command.execute()
    command = AddEntryCommand("2023/1/2", start_time, end_time, "task_date", ":TAGDATE", hours_spent)
    command.execute()
    command = AddEntryCommand("2023/1/3", start_time, end_time, "example task", ":TAGTASK", hours_spent)
    command.execute()
    command = AddEntryCommand("2022/1/4", start_time, end_time, "task_tag", ":TASKTAG", hours_spent)
    command.execute()

    start_date = "2023/1/01"
    end_date = "2023/12/31"

    command = ReportCommand(start_date, end_date)
    res = command.execute()

    assert len(res) == 3

    command = AddEntryCommand("2023/1/4", start_time, end_time, "task_tag", ":TASKTAG", hours_spent)
    command.execute()

    command = ReportCommand(start_date, end_date)
    res = command.execute()

    assert len(res) == 4

def test_PriorityCommand():
    command = PriorityCommand()
    result = command.execute()

    assert isinstance(result, list)
