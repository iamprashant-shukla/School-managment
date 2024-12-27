import sqlite3

def connect_db():
   return sqlite3.connect("school_managment.db")

def get_teacher():
   conn = connect_db()
   c = conn.cursor()
   c.execute('''SELECT * FROM teachers''')
   teachers = c.fetchall()
   c.close()
   return teachers


def get_students():
   conn = connect_db()
   c = conn.cursor()
   c.execute('''SELECT * FROM students''')
   students = c.fetchall()
   c.close()
   return students


def add_teacher(name, email, phone, subject):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (name, email, phone, subject) VALUES (?, ?, ?, ?)", 
                   (name, email, phone, subject))
    conn.commit()
    conn.close()

def add_student(name, class_id, parent_name, parent_contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, class_id, parent_name, parent_contact) VALUES (?, ?, ?, ?)",
                   (name, class_id, parent_name, parent_contact))
    conn.commit()
    conn.close()

def get_classes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()
    conn.close()
    return classes