import os

from advent.year24.problem2.solution import count_safe_reports, is_report_safe, parse_reports


def test_parse_column_file():
    data_file_path = os.path.join(os.path.dirname(__file__), 'exampleA.txt')
    reports = parse_reports(data_file_path)

    assert reports[0] == [1,2,3,4,5]
    assert reports[1] == [1,2,3,4]
    assert reports[2] == [1,2,3]


def test_is_report_safe():
    assert is_report_safe([1,2])
    assert not is_report_safe([1,2,1])
    assert is_report_safe([1,2,4])
    assert not is_report_safe([1,2,7])
    assert is_report_safe([2,1])
    assert is_report_safe([4,2,1])
    assert not is_report_safe([7,2,1])

def test_is_report_safe_dampener():
    assert not is_report_safe([1,2,6])
    assert is_report_safe([1,2,6], dampen=True)
    assert not is_report_safe([1,7,3])
    assert is_report_safe([1,7,3], dampen=True)
    assert is_report_safe([1,2,3,2,5], dampen=True)
    assert is_report_safe([5,4,7,8], dampen=True)



def test_example():
    data_file_path = os.path.join(os.path.dirname(__file__), 'exampleB.txt')
    reports = parse_reports(data_file_path)

    assert 2 == count_safe_reports(reports)
    assert 4 == count_safe_reports(reports, True)