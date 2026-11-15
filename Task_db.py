import sqlite3

def create_tables():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            task TEXT,
            complete BOOLEAN DEFAULT False,
            date TEXT
         )
     ''')
    conn.commit()
    conn.close()

def save_task(title,task,complete,date):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
         INSERT INTO tasks(title,task,complete,date)
         VALUES (?,?,?,?)''',(title,task,complete,date,))
    conn.commit()
    conn.close()

def get_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    task = cursor.fetchall()
    conn.close()
    return task

def search_task(search):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("select * FROM tasks Where title LIKE ?",('%'+search+'%',))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    conn.commit()
    conn.close()

def change_status(status_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("update tasks SET complete = not complete WHERE id = ?",(status_id,))
    conn.commit()
    conn.close()

def completed_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE complete = True")
    complete = cursor.fetchall()
    conn.commit()
    conn.close()
    return complete

if __name__ == "__main__":
    create_tables()
    print("your table is ready")
