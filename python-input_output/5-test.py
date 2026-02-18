import pytest

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
read_file = __import__('0-read_file').read_file


class TestSaveToJsonFile():
    filename = "test_file.txt"
    

    def test_save_to_json_file_exists(self):
        my_obj = [1, 2, 3]
        save_to_json_file(my_obj, self.filename)

    def test_save_to_json_file_writes_input_to_file(self, capfd):
        my_obj = 45
        save_to_json_file(my_obj, self.filename)
        read_file(self.filename)
        out, err = capfd.readouterr()
        assert out.split("\n")[-1] == "45"

    def test_save_to_json_file_converts_python_object_to_json(self):
        my_obj = [4, 5, 6]
        result = save_to_json_file(my_obj, self.filename)
        assert isinstance(result, str)
