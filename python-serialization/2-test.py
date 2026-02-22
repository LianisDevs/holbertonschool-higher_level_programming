import pytest
convert_csv_to_json = __import__("task_02_csv").convert_csv_to_json

class TestConvertCsvToJsonClass():

    def test_convert_csv_to_json_exists(self):
        convert_csv_to_json("data.csv")

    def test_convert_to_csv_returns(self):
        result = convert_csv_to_json("data.csv")
        assert result == True

    def test_convert_to_csv_handles_file_not_found(self):
        result = convert_csv_to_json("notARealFile.csv")
        assert result == False

