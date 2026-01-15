from python.db import get_db_connection , delete_student_by_id_db

# def add_student(list_name , id , name , age , marks):
#     list_name.append({
#             "id":id,
#             "name":name,
#             "age":age,
#             "marks":marks,
#             })
    
# def view_students(list_name):
#     if len(list_name) == 0:
#         print("NO RECORDS FOUND")
#     else:
#         for i in list_name:
#             print(i)

# def search_student(list_name , s_id):
#     for i in list_name:
#         if i["id"] == s_id:
#             print(i)
#             return
#     print("Student Not Found in List")
        
# def delete_student(list_name  , s_id):
#     for i in list_name:
#         if i["id"] == s_id:
#             list_name.remove(i)
#             print("Student deleted")
#             return 
#     print("No record to delete")

# students = []

def add_student_db(student_id , name , age , marks):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (id , name , age , marks) VALUES (? , ? , ? , ?)" , (student_id , name , age , marks))
    conn.commit()
    conn.close()


def get_all_students_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id , name , age , marks FROM students")
    rows = cursor.fetchall()
    conn.close()

    # Convert sqlite rows to list of dicts
    students = []
    for i in rows:
        students.append({
            "id":i["id"],
            "name":i["name"],
            "age":i["age"],
            "marks":i["marks"]
        })
    return students


def get_student_by_id_db(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?" , (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    
    return{
        "id":row["id"],
        "name":row["name"],
        "age":row["age"],
        "marks":row["marks"]
        }

def delete_student_db(s_id):
    return delete_student_by_id_db(s_id)

    



