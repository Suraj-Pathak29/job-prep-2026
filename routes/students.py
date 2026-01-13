from flask import Blueprint , jsonify , request , abort
from python.student_logic import students , add_student 
students_bp = Blueprint("students" , __name__)


# GET + POST (collection)
@students_bp.route("/students" , methods = ["GET" , "POST"])
def students_handler():
    if request.method == "GET":
            return jsonify(students)
    
    if request.method == "POST":
        data = request.get_json()
        
        #JSON existence check
        if not data:
              abort(400)
        
        #Required field validation
        required_fields = ["id" , "name" , "age" , "marks"]
        for field in required_fields:
              if field not in data:
                    return jsonify({"error":f"{field} is required"}),400
    
        #Type validation
        if not isinstance(data["id"] , int):
              return jsonify({"error":"id must be an integer"}),400
        
        #Type validation
        if not isinstance(data["name"] , str):
              return jsonify({"error":"name must be a string"}),400
        
        #Business rule validation
        if not data["name"].strip():
              return jsonify({"error":"name cannot be empty"}),400
        
        #Type validation
        if not isinstance(data["age"] , int):
              return jsonify({"error":"age must be an integer"}),400
        
        #Business rule validation
        if data["age"] <= 0:
              return jsonify({"error":"age must be positive"}),400
        
        #Type validation
        if not isinstance(data["marks"] , int):
              return jsonify({"error":"marks must be an integer"}),400
        
        #Business rule validation
        if data["marks"] < 0 or data["marks"] > 100:
              return jsonify({"error":"marks must be between 0 and 100"}),400

        add_student(
            students,
            data["id"],
            data["name"],
            data["age"],
            data["marks"]
            )
        return jsonify({"message" : "student added successfully"}),201
    

# DELETE (single student)
@students_bp.route("/students/<int:s_id>" , methods = ["DELETE"])
def delete_student_api(s_id):
            for i in students:
                   if i["id"] == s_id:
                        students.remove(i)
                        return jsonify({"message":"Student deleted successfully"}),200
                   
            return jsonify({"error":"Student not found"}),404