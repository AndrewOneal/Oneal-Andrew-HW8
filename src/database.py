import sqlite3
from datetime import datetime

class DatabaseController:

    def __init__(self):
        self.con = sqlite3.connect("timetracker.db")
        self.cur = self.con.cursor()
        self.addTable()

    def addTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS TaskEntries (
            id integer PRIMARY KEY,
            date text,
            time_from text,
            time_to text,
            task text, 
            tag text
            )''')

    def addEntry(self, date, time_from, time_to, task, tag):
        self.cur.execute('''INSERT INTO TaskEntries (
            date,
            time_from,
            time_to,
            task,
            tag
            ) 
            VALUES (?, ?, ?, ?, ?)
        ''', (date, time_from, time_to, task, tag))
        self.con.commit()

    def retrieveAllEntries(self):
        self.cur.execute("SELECT * FROM TaskEntries")
        rows = self.cur.fetchall()
        return rows

    def retrieveTaskEntriesByTag(self, tag):
        self.cur.execute(f"SELECT * FROM TaskEntries WHERE tag=?", (tag,))
        rows = self.cur.fetchall()
        return rows
    
    def retrieveTaskEntriesByDate(self, date):
        self.cur.execute(f"SELECT * FROM TaskEntries WHERE date=?", (date,))
        rows = self.cur.fetchall()
        return rows
    
    def retrieveTaskEntriesByTag(self, task):
        self.cur.execute(f"SELECT * FROM TaskEntries WHERE tag=?", (task,))
        rows = self.cur.fetchall()
        return rows

    def deleteAll(self):
        self.cur.execute("DELETE FROM TaskEntries")

if __name__ == "__main__":
    db = DatabaseController()
    db.addTable()
    db.addEntry('12/8/2023', '12:42', '12:56', 'wrote code', ':CODING')
    db.addEntry('12/8/2023', '12:42', '12:56', 'wrote code', ':SLEEPING')
    data = db.retrieveTaskEntriesByTag(":SLEEPING")
    print(data)
    db.deleteAll()
    data = db.retrieveAllEntries()
    print(data)