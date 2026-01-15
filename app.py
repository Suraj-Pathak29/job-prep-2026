from flask import Flask , jsonify 
from routes.students import students_bp 
from python.db import create_students_table

app = Flask(__name__)

create_students_table()

app.register_blueprint(students_bp)

@app.errorhandler(400)
def bad_request(error):
      return jsonify({
            "status":"error",
            "message":"Bad request"}),400

@app.errorhandler(404)
def not_found(error):
      return jsonify({
            "status":"error",
            "message":"Resource not found"}),404



if __name__ == "__main__":
    app.run(debug=True) 