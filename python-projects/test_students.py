import unittest
from student import Students

class TestStudents(unittest.TestCase):

    def setUp(self):
        Students._id_counter = 1
        self.student=Students("Ann", "100", "Computer Science", 3.5)

    def test_add_student(self):
        result = self.student.add_student()
        self.assertEqual(result, f"New student Ann with student ID {self.student.student_id} has been added to records.")

    def test_update_record(self):
        result = self.student.update_record()
        self.assertEqual(result, f"Student with name Ann record has gpa 3.5 updated." )

    def test_remove_student(self):
        results = self.student.remove_student()
        self.assertEqual(results, f"Student with name Ann and ID {self.student.student_id} has been removed.")

    def test_to_dict(self):
        results=self.student.to_dict()
        expected = {
            "student_id": self.student.student_id,
            "name": "Ann",
            "level": "100",
            "course": "Computer Science",
            "gpa": 3.5
        }
        self.assertEqual(results, expected)
            
if __name__ == '__main__':
    unittest.main()

