import pytest
Student = __import__('10-student').Student

class TestStudentClass():
    def test_student_class_exists(self):
        student = Student("John", "Doe", 23)
        assert isinstance(student, Student)

    def test_student_has_to_json(self):
        student = Student("John", "Doe", 23)
        result = student.to_json()
        assert isinstance(result, dict)
        assert "first_name" in result

    def test_student_to_json_attr_check(self):
        student = Student("John", "Doe", 23)
        result = student.to_json("age")
        assert "age" in result

    def test_student_to_json_attr_check_multi_attrs(self):
        student = Student("John", "Doe", 23)
        result = student.to_json(["age", "first_name"])
        assert "age" in result
        assert "first_name" in result

    def test_student_to_json_handles_invalid_input(self):
        student = Student("John", "Doe", 23)
        result = student.to_json([1, 2, 3])
        assert "age" in result
        assert "first_name" in result
        assert "last_name" in result

    def test_student_to_json_handles_invalid_input_with_valid_input(self):
        student = Student("John", "Doe", 23)
        result = student.to_json([1, "age", "first_name"])
        assert "age" in result
        assert "first_name" in result
        assert "last_name" in result

