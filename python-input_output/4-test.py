import pytest
import json

from_json_string = __import__('4-from_json_string').from_json_string

class TestFromJsonStringClass():

    def test_from_json_string_exists(self):
        my_str = "[1, 2, 3]"
        from_json_string(my_str)

    def test_from_json_string_returns_object(self):
        my_str = "[1, 2, 3]"
        result = from_json_string(my_str)
        assert result == [1, 2, 3]

    def test_from_json_string_handles_int(self):
        with pytest.raises(TypeError):
            from_json_string(1)

    def test_from_json_string_handles_corrupted_json(self):
        s_my_dict = """
        {"is_active": true, 12 }
        """
        with pytest.raises(json.JSONDecodeError):
            from_json_string(s_my_dict)
