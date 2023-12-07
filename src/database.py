import sqlite3
from datetime import datetime

class DatabaseController:

    def __init__(self):
        self.con = sqlite3.connect("timetracker.db")
        self.cur = self.con.cursor()
        self.addTable()

    def addTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS TaskEntries (
            id integer PRIMARY KEY AUTOINCREMENT,
            date text,
            start_time text,
            end_time text,
            task text, 
            tag text
            )''')

    def addEntry(self, date, start_time, end_time, task, tag):
        self.cur.execute('''INSERT INTO TaskEntries (
            date,
            start_time,
            end_time,
            task,
            tag
            ) 
            VALUES (?, ?, ?, ?, ?)
        ''', (date, start_time, end_time, task, tag))
        self.con.commit()

    def queryAllEntries(self):
        self.cur.execute("SELECT * FROM TaskEntries")
        rows = self.cur.fetchall()
        return rows

    def queryEntry(self, date=None, task=None, tag=None):
        query = 'SELECT * FROM TaskEntries WHERE i=i'
        params = []

        if date: 
            params.append(date)
            query += ' AND date = ?'
        if task:
            params.append(task)
            query += ' AND task = ?'
        if tag:
            params.append(tag)
            query += ' AND tag = ?'

        self.cur.execute(query, params)
        
        entries = self.cur.fetchall()
        return entries

    def deleteAll(self):
        self.cur.execute("DELETE FROM TaskEntries")

if __name__ == "__main__":
    db = DatabaseController()
    print(db.con)