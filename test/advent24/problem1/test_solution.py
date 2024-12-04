from advent24.problem1.solution import parse_column_file, get_heap_corresponding_difference
import os

def test_parse_column_file():
    data_file_path = os.path.join(os.path.dirname(__file__), 'exampleA.txt')
    heapA, heapB = parse_column_file(data_file_path)

    assert heapA == [1,2,3,4,5]
    assert heapB == [1,2,3,4,5]

    assert get_heap_corresponding_difference(heapA, heapB) == 0

def test_get_heap_corresponding_difference():
    heapA = [1,2,3,4,5]
    heapB = [1,2,3,4,6]

    assert get_heap_corresponding_difference(heapA, heapB) == 1