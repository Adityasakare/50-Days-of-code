import sqlite3

db = 'my_todo.db'

table_name = 'tasks'
conn = sqlite3.connect(db)

c = conn.cursor() #Responsible for Actions

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + \
    '(ID INTEGER PRIMARY KEY AUTOINCREMENT, TaskName Text )'

    c.execute(sql)

def data_entry(task):
    c.execute("INSERT INTO " + table_name + "(TaskName) VALUES (?), [task]")
    print("Task is added in database")
    conn.commit()

def PrintData():
   sql = "SELECT * FROM " + table_name
   c.execute(sql)

def DeleteTask(index):
    c.execute('DELETE FROM ' + table_name + ' WHERE ID=?', (index, ))
    print("Task is deleted from database")

def closeCursor():
    c.close()
    conn.close()

