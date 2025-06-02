''' This is a student records app'''

from flask import Flask, request, jsonify
from student import Students

records_api = Flask(__name__)

Students_records = {}

@records_api.route("/records", methods= ['POST'])
def post_student():
    
    data = request.get_json()

    name = data.get ('name')
    level = data.get('level')
    course = data.get('course')
    gpa = data.get ('gpa')

    if not all ([name, level, course, gpa]):
        return jsonify ({'error': 'missing fields'}), 400
    
    student = Students (name, level, course, gpa)
    Students_records[student.student_id] = student

    return jsonify({
        'message': student.add_student(),
        'student' : student.to_dict ()

    }), 201

@records_api.route("/records", methods=["GET"])
def get_students():
    return jsonify([student.to_dict() for student in Students_records.values()])


@records_api.route("/records/<int:student_id>", methods=["PATCH"])
def update_students(student_id):
    data = request.get_json()
    
    student = Students_records.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    if "name" in data:
        student.name = data["name"]
    if "level" in data:
        student.level = data["level"]
    if "course" in data:
        student.course = data["course"]
    if "gpa" in data:
        student.gpa = data["gpa"]

    return jsonify({
        "message": f"Student {student_id} updated.",
        "student": student.to_dict()
    })




if __name__ == '__main__':
  records_api.run(debug=True)