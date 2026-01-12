# LIST FORMAT
# students=[{"id":1 , "name":"Rahul" , "age":20 , "marks":85}]

# PSEUDOCODE
# students = empty list

# LOOP forever:
#     show menu options
#     ask user for choice

#     IF choice is add:
#         take student details
#         add student

#     ELSE IF choice is view:
#         show students

#     ELSE IF choice is search:
#         ask id
#         search student

#     ELSE IF choice is delete:
#         ask id
#         delete student

#     ELSE IF choice is exit:
#         stop loop

#     ELSE:
#         show invalid choice



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
            print("Student record deleted")
            return 
    print("No record to delete")


student = []
print("Welcome!!")

# add , view , search , delete , exit

valid = True
while valid:
    print("Menu Options:")
    print("Press(1) -- ADD STUDENTS")
    print("Press(2) -- VIEW STUDENT")
    print("Press(3) -- SEARCH STUDENT")
    print("Press(4) -- DELETE STUDENT")
    print("Press(5) -- EXIT")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        t_id = int(input("Enter student id: "))
        t_name = input("Enter student name: ")
        t_age = int(input("Enter student's age: "))
        t_marks = int(input("Enter student's marks: "))
        add_student(student , t_id , t_name , t_age , t_marks)
        print("Student record added!")

    elif ch == 2:
        view_students(student)


    elif ch == 3:
        a = int(input("Enter student's ID: "))
        search_student(student , a)


    elif ch == 4:
        x = int(input("Enter student's ID: "))
        delete_student(student , x)


    elif ch == 5:
        print("Thank You for using!")
        valid = False
        break

    else:
        print("INVALID CHOICE!")
        print("Please enter (1 - 5)")


        