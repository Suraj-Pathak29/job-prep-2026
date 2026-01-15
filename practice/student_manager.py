# LIST FORMAT
# students=[{"id":1 , "name":"Rahul" , "age":20 , "marks":85}]

def add_student(list_name , id , name , age , marks):
    list_name.append({
            "id":id,
            "name":name,
            "age":age,
            "marks":marks,
            })
    
def view_students(list_name):
    if len(list_name) == 0:
        print("NO RECORDS FOUND")
    else:
        for i in list_name:
            print(i)

def search_student(list_name , s_id):
    for i in list_name:
        if i["id"] == s_id:
            print(i)
            return
    print("Student Not Found in List")
        
def delete_student(list_name  , s_id):
    for i in list_name:
        if i["id"] == s_id:
            list_name.remove(i)
            print("Student deleted")
            return 
    print("No record to delete")


students=[]
add_student(students,1,"Rahul",20,85)
add_student(students,2,"Anita",22,90)
add_student(students,3,"Suraj",21,78)
view_students(students)    
delete_student(students,5)
search_student(students,4)