from contextlib import nullcontext as does_not_raise
import pytest
import io
read_file = __import__('0-read_file').read_file

class TestReadFileClass():
    test_file = "test_file.txt"

    def test_read_file_exists(self):
        read_file()

    def test_read_file_handles_no_file(self):
        read_file()

    def test_read_file_open(self):
        try:
            read_file(self.test_file)
        except FileNotFoundError:
            raise pytest.fail("Exception Raised, File not found - test failed")

    def test_read_file_reads(self, capfd):
        read_file(self.test_file)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "Hello, World!"
