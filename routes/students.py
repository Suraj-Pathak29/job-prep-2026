from flask import Blueprint , jsonify , request , abort
from python.student_logic import students , add_student_db , get_all_students_db ,get_student_by_id_db , delete_student_db
students_bp = Blueprint("students" , __name__)


# GET + POST (collection)
@students_bp.route("/students" , methods = ["GET" , "POST"])
def students_handler():
    if request.method == "GET":
            students = get_all_students_db()
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

        add_student_db(
              data["id"],
              data["name"],
              data["age"],
              data["marks"]
        )
        return jsonify({"message" : "student added successfully"}),201
    

#GET (Single Student)
@students_bp.route("/students/<int:s_id>" , methods = ["GET"])
def get_single_student(s_id):
      student = get_student_by_id_db(s_id)
      if student is None:
            abort(404)
      return jsonify(student),200
    

# DELETE (single student)
@students_bp.route("/students/<int:s_id>" , methods = ["DELETE"])
def delete_student(s_id):
      deleted = delete_student_db(s_id)
      if not deleted:
            abort(404)
      return jsonify({"message":"student deleted successfully"}),200
