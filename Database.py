import sqlite3

#it creates the database if it not exist 
connect = sqlite3.connect("school_managment.db")

#define the cursor
c = connect.cursor()

# Create tables
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        subject TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        class_id INTEGER,
        parent_name TEXT NOT NULL,
        parent_contact TEXT NOT NULL,
        FOREIGN KEY (class_id) REFERENCES classes (class_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS classes (
        class_id INTEGER PRIMARY KEY,
        class_name TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS class_teacher (
        class_id INTEGER,
        teacher_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES classes (class_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS class_student (
        class_id INTEGER,
        student_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES classes (class_id),
        FOREIGN KEY (student_id) REFERENCES students (student_id)
    )
''')


#if you want to use some sample data then uncomment it or else ignore.

'''
# Insert some sample data

# Users (Principal, Teacher)
c.execute("INSERT INTO users (username, password, role) VALUES ('principal1', 'password123', 'principal')")
c.execute("INSERT INTO users (username, password, role) VALUES ('teacher1', 'password123', 'teacher')")

# Teachers
c.execute("INSERT INTO teachers (name, email, phone, subject) VALUES ('John Doe', 'john@example.com', '1234567890', 'Mathematics')")
c.execute("INSERT INTO teachers (name, email, phone, subject) VALUES ('Jane Smith', 'jane@example.com', '0987654321', 'Computer Science')")

# Classes
c.execute("INSERT INTO classes (class_name) VALUES ('Class 1')")
c.execute("INSERT INTO classes (class_name) VALUES ('Class 2')")

# Class-Teacher Assignments
c.execute("INSERT INTO class_teacher (class_id, teacher_id) VALUES (1, 1)")  # John Doe teaches Class 1
c.execute("INSERT INTO class_teacher (class_id, teacher_id) VALUES (2, 2)")  # Jane Smith teaches Class 2

# Students
c.execute("INSERT INTO students (name, class_id, parent_name, parent_contact) VALUES ('Student A', 1, 'Parent A', '1234567890')")
c.execute("INSERT INTO students (name, class_id, parent_name, parent_contact) VALUES ('Student B', 2, 'Parent B', '0987654321')")

# Class-Student Assignments
c.execute("INSERT INTO class_student (class_id, student_id) VALUES (1, 1)")  # Student A in Class 1
c.execute("INSERT INTO class_student (class_id, student_id) VALUES (2, 2)")  # Student B in Class 2

'''

# Commit the changes and close the connection
connect.commit()
connect.close()

print("Database initialized Successfully")
