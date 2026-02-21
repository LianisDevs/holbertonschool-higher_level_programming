import pytest
Student = __import__('9-student').Student

class TestStudentClass():
    def test_student_class_exists(self):
        student = Student("John", "Doe", 23)
        assert isinstance(student, Student)

    def test_student_has_to_json(self):
        student = Student("John", "Doe", 23)
        result = student.to_json()
        assert isinstance(result, dict)
        assert "first_name" in result
