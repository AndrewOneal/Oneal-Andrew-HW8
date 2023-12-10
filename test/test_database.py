import pytest
import sys
import sqlite3
import os
sys.path.append('src')
from database import DatabaseController

@pytest.fixture
def db():
    yield DatabaseController()

def test_addTable(db):
    db.addTable()
    db.deleteAll()

def test_add_entry():

    db = DatabaseController()

    date = "2023/01/01"
    start_time = "10:00AM"
    end_time = "11:00AM"
    task = "Sample Task"
    tag = ":SAMPLETAG"

    db.addEntry(date, start_time, end_time, task, tag)

    entries = db.queryAllEntries()
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

    db.addEntry(date, start_time, end_time, task, tag)
    entries = db.queryAllEntries()

    assert len(entries) == 2
    assert entries[1][1] == date
    assert entries[1][2] == start_time
    assert entries[1][3] == end_time
    assert entries[1][4] == task
    assert entries[1][5] == tag

    db.deleteAll()

def test_queryAllEntries():
    db = DatabaseController()

    start_time = "10:00PM"
    end_time = "11:00PM"

    db.addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    db.addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    db.addEntry("2023/1/2", start_time, end_time, "example task", ":TAGTASK")
    db.addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    res = db.queryAllEntries()
    assert len(res) == 4

    for entry in res:
        assert len(entry) == 6
        assert isinstance(entry[0], int)

def test_queryEntry(db):
    db = DatabaseController()

    start_time = "10:00PM"
    end_time = "11:00PM"

    db.addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    db.addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    db.addEntry("2023/1/2", start_time, end_time, "example task", ":TAGTASK")
    db.addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    res = db.queryEntry(date="today")
    assert(res[0][1] == "today")
    assert(res[0][4] == "task_today")
    assert(res[0][5] == ":TAGTODAY")

    res = db.queryEntry(date="2023/1/1")
    assert(res[0][1] == "2023/1/1")
    assert(res[0][4] == "task_date")
    assert(res[0][5] == ":TAGDATE")
    
    res = db.queryEntry(task="example task")
    assert(res[0][1] == "2023/1/2")
    assert(res[0][4] == "example task")
    assert(res[0][5] == ":TAGTASK")
    
    res = db.queryEntry(tag=":TASKTAG")
    assert(res[0][1] == "2023/1/3")
    assert(res[0][4] == "task_tag")
    assert(res[0][5] == ":TASKTAG") 

    db.deleteAll()

    

def test_deleteAll(db):
    db = DatabaseController()

    start_time = "10:00PM"
    end_time = "11:00PM"

    db.addEntry("today", start_time, end_time, "task_today", ":TAGTODAY")
    db.addEntry("2023/1/1", start_time, end_time, "task_date", ":TAGDATE")
    db.addEntry("2023/1/2", start_time, end_time, "example task", "TAGTASK")
    db.addEntry("2023/1/3", start_time, end_time, "task_tag", ":TASKTAG")

    entries_before_delete = db.queryAllEntries()
    assert len(entries_before_delete) == 4 

    db.deleteAll()

    entries_after_delete = db.queryAllEntries()
    assert len(entries_after_delete) == 0

