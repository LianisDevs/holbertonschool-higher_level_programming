import pytest

append_write = __import__('2-append_write').append_write
read_file = __import__('0-read_file').read_file

class TestAppendWriteClass():
    test_file = "test_file.txt"
    new_text = "What like it's hard?\n"
    text = "Testing\n"

    def test_append_write_exists(self):
        append_write(self.test_file, self.text)

    def test_append_write_appends_text_at_end_of_file(self, capfd):
        append_write(self.test_file, self.new_text)
        read_file(self.test_file)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "What like it's hard?"

    def test_append_write_returns_num_chars_written(self):
        result = append_write(self.test_file, self.new_text)
        assert result == 21
