import pytest

to_json_string = __import__('3-to_json_string').to_json_string

class TestToJsonStringClass():
    my_obj = [1, 2, 3]

    def test_to_json_string_exists(self):
       to_json_string(self.my_obj)

    def test_to_json_string_returns_json_representation(self):
        result = to_json_string(self.my_obj)
        assert isinstance(result, str)
