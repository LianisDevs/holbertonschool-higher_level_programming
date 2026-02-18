import pytest

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

class TestLoadFromJsonFileClass():

    def test_load_from_json_file_exists(self):
        load_from_json_file("my_list.json")

    def test_load_from_json_file_creates_object(self):
        obj = load_from_json_file("my_list.json")
        assert isinstance(obj, list)
