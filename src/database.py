import sqlite3

class DatabaseController:

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseController, cls).__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.con = sqlite3.connect("timetracker.db")
            self.cur = self.con.cursor()
            self.addTable()

    def __del__(self):
        self.con.close()
        
    def addTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS TaskEntries (
            id integer PRIMARY KEY AUTOINCREMENT,
            date text,
            start_time text,
            end_time text,
            task text, 
            tag text,
            hours_spent real
            )''')

    def addEntry(self, date, start_time, end_time, task, tag, hours_spent):
        self.cur.execute('''INSERT INTO TaskEntries (
            date,
            start_time,
            end_time,
            task,
            tag,
            hours_spent
            ) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, start_time, end_time, task, tag, hours_spent))
        self.con.commit()

    def queryAllEntries(self):
        self.cur.execute("SELECT * FROM TaskEntries")
        rows = self.cur.fetchall()
        return rows

    def queryEntry(self, date=None, task=None, tag=None):
        query = 'SELECT date, start_time, end_time, task, tag FROM TaskEntries WHERE'
        params = []

        if date: 
            params.append(date)
            query += ' date = ?'
        if task:
            params.append(task)
            query += ' task = ?'
        if tag:
            params.append(tag)
            query += ' tag = ?'

        self.cur.execute(query, tuple(params))
        
        entries = self.cur.fetchall()
        return entries

    def deleteAll(self):
        self.cur.execute("DROP TABLE IF EXISTS TaskEntries")
        self.addTable()

    def queryReport(self, start_date, end_date):
        query = 'SELECT date, start_time, end_time, task, tag FROM TaskEntries WHERE date BETWEEN ? AND ?'
        params = (start_date, end_date)
        self.cur.execute(query, params)
        entries = self.cur.fetchall()
        return entries
    
    def queryPriority(self):
        query = 'SELECT task, SUM(hours_spent) AS total_hours FROM TaskEntries GROUP BY task ORDER BY total_hours DESC'
        self.cur.execute(query)
        task_hours = self.cur.fetchall()
        return task_hours
    
    def close(self):
        self.con.close()