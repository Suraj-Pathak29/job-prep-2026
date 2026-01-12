from flask import Flask , jsonify , request
from python.student_logic import students , add_student 

app = Flask(__name__)

# GET + POST (collection)
@app.route("/students" , methods = ["GET" , "POST"])
def students_handler():
    if request.method == "GET":
            return jsonify(students)
    
    if request.method == "POST":
        data = request.get_json()
        add_student(
            students,
            data["id"],
            data["name"],
            data["age"],
            data["marks"]
            )
        return jsonify({"message" : "student added successfully"}),201

# DELETE (single student)
@app.route("/students/<int:s_id>" , methods = ["DELETE"])
def delete_student_api(s_id):
            for i in students:
                   if i["id"] == s_id:
                        students.remove(i)
                        return jsonify({"message":"Student deleted successfully"}),200
                   
            return jsonify({"error":"Student not found"}),404
              
if __name__ == "__main__":
    app.run(debug=True)