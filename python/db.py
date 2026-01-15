import sqlite3

def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row 
    return conn

def create_students_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS students
                   (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   marks INTEGER NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()

def delete_student_by_id_db(s_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (s_id,)
        )
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()

    return deleted_rows > 0
