from advent.year24.problem1.solution import parse_column_file, get_list_corresponding_difference, get_similarity_score
import os

def test_parse_column_file():
    data_file_path = os.path.join(os.path.dirname(__file__), 'exampleA.txt')
    listA, listB = parse_column_file(data_file_path)

    assert listA == [1,2,3,4,5]
    assert listB == [5,4,3,2,1]

def test_get_list_corresponding_difference():
    listA = [3,4,2,1,3,3]
    listB = [4,3,5,3,9,3]

    assert get_list_corresponding_difference(listA, listB) == 11

def test_get_similarity_score():
    listA = [3,4,2,1,3,3]
    listB = [4,3,5,3,9,3]

    assert get_similarity_score(listA, listB) == 31