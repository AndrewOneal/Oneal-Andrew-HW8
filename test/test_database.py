import pytest
import sys
import sqlite3
sys.path.append('src')
from database import DatabaseController

@pytest.fixture
def db():
    yield DatabaseController()

def test_addTable(db):
    db.addTable()

def test_add_entry(db):
    db.deleteAll()

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


def test_queryAllEntries(db):
    pass

def test_queryEntry(db):
    pass

def test_deleteAll(db):
    pass

