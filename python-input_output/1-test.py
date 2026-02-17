from os import write
import pytest
read_file = __import__('0-read_file').read_file
write_file = __import__('1-write_file').write_file

class TestWriteFileClass():
    test_file = "test_file.txt"
    new_text = "This is fun!\n"

    def test_write_file_exists(self):
        write_file(self.test_file, self.new_text)

    def test_write_file_overwrites_input_to_file(self, capfd):
        write_file(self.test_file, self.new_text)
        read_file(self.test_file)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "This is fun!"

    def test_write_file_returns_number_of_chars_written(self):
        result = write_file(self.test_file, self.new_text)
        assert result == 13


    def test_write_file_creates_and_writes_to_new_file(self, capfd):
        write_file("fake_file.txt", self.new_text)
        read_file(self.test_file)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "This is fun!"

    def test_write_file_no_file_given(self):
        write_file(self.new_text)

