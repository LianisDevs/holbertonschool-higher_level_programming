import pytest

CustomObject = __import__("task_01_pickle").CustomObject

class TestCustomObjectClass():

    def test_custom_class_exists(self):
        obj = CustomObject(name="John", age=25, is_student=True)
        assert obj.name == "John"
        assert obj.age == 25
        assert obj.is_student == True
        assert isinstance(obj, CustomObject)

    def test_custom_class_has_serialize(self):
        obj = CustomObject(name="John", age=25, is_student=True)
        obj.serialize("CustomObject.pkl")

    def test_custom_object_serialize_creates_file(self):
        obj = CustomObject(name="John", age=25, is_student=True)
        obj.serialize("CreateMe.pkl")

    def test_custom_object_has_deserialize(self):
        CustomObject.deserialize("CustomObject.pkl")

    def test_custom_object_deserialize_returns_object(self):
        loaded_object = CustomObject.deserialize("CreateMe.pkl")
        assert isinstance(loaded_object, CustomObject)
        assert loaded_object.name == "John"
        assert loaded_object.age == 25
        assert loaded_object.is_student == True

    def test_custom_object_has_display(self, capfd):
        obj = CustomObject(name="John", age=25, is_student=True)
        obj.display()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "Is Student: True"

