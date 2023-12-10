import pytest
import sys
import sqlite3
import os
sys.path.append('src')
from database import DatabaseController

def test_addTable():
    DatabaseController().addTable()
    DatabaseController().deleteAll()

def test_add_entry():

    date = "2023/01/01"
    start_time = "10:00AM"
    end_time = "11:00AM"
    task = "Sample Task"
    tag = ":SAMPLETAG"

    DatabaseController().addEntry(date, start_time, end_time, task, tag)

    entries = DatabaseController().queryAllEntries()
    assert len(entries) == 1
    assert entries[0][1] == date
    assert entries[0][2] == start_time
    assert entries[0][3] == end_time
    assert entries[0][4] == task
    assert entries[0][5] == tag

    date = "today"
    start_time = "10:00"
    end_time = "11:00"
    task = "Sample Task"
    tag = ":SAMPLETAG"

    DatabaseController().addEntry(date, start_time, end_time, task, tag)
    entries = DatabaseController().queryAllEntries()

    assert len(entries) == 2
    assert entries[1][1] == date
    assert entries[1][2] == start_time
    assert entries[1][3] == end_time
    assert entries[1][4] == task
    assert entries[1][5] == tag

    DatabaseController().deleteAll()

def test_queryAllEntries():
    start_time = "10:00PM"
    end_time = "11:00PM"

    DatabaseController().addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    DatabaseController().addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    DatabaseController().addEntry("2023/1/2", start_time, end_time, "example task", ":TAGTASK")
    DatabaseController().addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    res = DatabaseController().queryAllEntries()
    assert len(res) == 4

    for entry in res:
        assert len(entry) == 6
        assert isinstance(entry[0], int)

def test_queryEntry():

    start_time = "10:00PM"
    end_time = "11:00PM"

    DatabaseController().addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    DatabaseController().addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    DatabaseController().addEntry("2023/1/2", start_time, end_time, "example task", ":TAGTASK")
    DatabaseController().addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    res = DatabaseController().queryEntry(date="today")
    assert(res[0][1] == "today")
    assert(res[0][4] == "task_today")
    assert(res[0][5] == ":TAGTODAY")

    res = DatabaseController().queryEntry(date="2023/1/1")
    assert(res[0][1] == "2023/1/1")
    assert(res[0][4] == "task_date")
    assert(res[0][5] == ":TAGDATE")
    
    res = DatabaseController().queryEntry(task="example task")
    assert(res[0][1] == "2023/1/2")
    assert(res[0][4] == "example task")
    assert(res[0][5] == ":TAGTASK")
    
    res = DatabaseController().queryEntry(tag=":TASKTAG")
    assert(res[0][1] == "2023/1/3")
    assert(res[0][4] == "task_tag")
    assert(res[0][5] == ":TASKTAG") 

    DatabaseController().deleteAll()

    

def test_deleteAll():

    start_time = "10:00PM"
    end_time = "11:00PM"

    DatabaseController().addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    DatabaseController().addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    DatabaseController().addEntry("2023/1/2", start_time, end_time, "example task", "TAGTASK")
    DatabaseController().addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    entries_before_delete = DatabaseController().queryAllEntries()
    assert len(entries_before_delete) == 4 

    DatabaseController().deleteAll()

    entries_after_delete = DatabaseController().queryAllEntries()
    assert len(entries_after_delete) == 0

def test_queryReport():
    DatabaseController().addEntry("2023-01-01", "10:00", "12:00", "Test Task", "Test Tag")
    DatabaseController().addEntry("2023-01-02", "14:00", "16:00", "Another Task", "Another Tag")

    start_date = "2023-01-01"
    end_date = "2023-01-02"
    result = DatabaseController().queryReport(start_date, end_date)

    assert len(result) == 2  

    DatabaseController().deleteAll()
