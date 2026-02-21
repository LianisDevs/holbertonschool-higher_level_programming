import pytest

MyClass = __import__('8-class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

class TestClassToJson():

    def test_class_to_json_exists(self):
        obj = MyClass("John", 89)
        obj_json = class_to_json(obj)
        assert isinstance(obj_json, dict)
