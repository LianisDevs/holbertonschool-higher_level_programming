import pytest

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

class TestPascalTriangleClass():
    def test_pascal_triangle_exists(self):
        result = pascal_triangle(1)
        assert isinstance(result, list)
