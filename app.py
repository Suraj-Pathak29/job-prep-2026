from flask import Flask , jsonify 
from routes.students import students_bp  

app = Flask(__name__)

app.register_blueprint(students_bp)

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