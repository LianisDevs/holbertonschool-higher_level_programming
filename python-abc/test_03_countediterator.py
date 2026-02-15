import pytest
from collections.abc import Iterator
from task_03_countediterator import CountedIterator

class TestCountedIteratorClass():
    data = [1, 2, 3]

    def test_counted_iterator_exists(self):
        counted_iterator = CountedIterator(self.data)
        assert isinstance(counted_iterator, CountedIterator)

    def test_counted_iterator_initializes(self):
        counted_iterator = CountedIterator(self.data)
        real_iterator = iter(self.data)
        assert hasattr(counted_iterator, "counter")
        assert hasattr(counted_iterator, "iterator")
        assert isinstance(counted_iterator.counter, int)
        assert isinstance(counted_iterator.iterator, Iterator)

    def test_counted_iterator_has_get_count(self):
        counted_iterator = CountedIterator(self.data)
        result = counted_iterator.get_count()
        assert result == 0

    def test_counter_iterator__next(self):
        counted_iterator = CountedIterator(self.data)
        result = counted_iterator.__next__()
        assert result == 1
        result = counted_iterator.__next__()
        assert result == 2

    def test_counted_iterator_next_increments_counter(self):
        counted_iterator = CountedIterator(self.data)
        result = counted_iterator.__next__()
        assert counted_iterator.get_count() == 1
        result = counted_iterator.__next__()
        assert counted_iterator.get_count() == 2

    def test_counted_iterator_has_stop_iteration_exception(self): with pytest.raises(StopIteration):
            counted_iterator = CountedIterator(self.data)
            counted_iterator.__next__()
            counted_iterator.__next__()
            counted_iterator.__next__()
            counted_iterator.__next__()
