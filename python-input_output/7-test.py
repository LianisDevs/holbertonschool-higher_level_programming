import pytest
import sys

load_item = __import__('6-load_from_json_file').load_from_json_file
add_item = __import__('7-add_item').add_item

class TestAddItemClass():

    def test_add_item_exists(self):
        add_item('test_file.json')
    def test_appends_data_to_file(self, monkeypatch, capfd):
        monkeypatch.setattr(sys, 'argv', ['./7-add_item.py', 1, 2, 3])
        add_item('test_save_file.json')
        file = load_item('test_save_file.json')
        assert file == [1, 2, 3]
        
