from flask import Flask , jsonify , request , abort
from python.student_logic import students , add_student 

app = Flask(__name__)

# GET + POST (collection)
@app.route("/students" , methods = ["GET" , "POST"])
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
@app.route("/students/<int:s_id>" , methods = ["DELETE"])
def delete_student_api(s_id):
            for i in students:
                   if i["id"] == s_id:
                        students.remove(i)
                        return jsonify({"message":"Student deleted successfully"}),200
                   
            return jsonify({"error":"Student not found"}),404
              

@app.errorhandler(400)
def bad_request(error):
      return jsonify({
            "status":"error",
            "message":"Bad request"}),400

app.errorhandler(404)
def not_found(error):
      return jsonify({
            "status":"error",
            "message":"Resource not found"}),404



if __name__ == "__main__":
    app.run(debug=True)