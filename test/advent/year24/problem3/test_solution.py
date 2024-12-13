from advent.year24.problem3.solution import do_dont_sum_corrupted_mul_instructions, is_valid_int_arg, sum_corrupted_mul_instructions


def test_solution():
    tests = [
        ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161),
        ("ASFDmul(012,999)123", 12* 999),
        ("mul (2,4,)", 0),
        ("mul ( 2, 4)", 0),
        ("mul ( 2, 4)", 0),("mul(0002,1)", 0),
        ("Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing", 0),
        ("mul(-2,1)", 0),
        ("mul('2',1)", 0),
    ]

    for input, expected in tests:
        assert sum_corrupted_mul_instructions(input) == expected

def test_do_dont():
    tests = [
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48)
    ]

    for input, expected in tests:
        assert do_dont_sum_corrupted_mul_instructions(input) == expected

def test_is_valid_int_arg():
    assert is_valid_int_arg("1")
    assert is_valid_int_arg("111")
    assert not is_valid_int_arg("-1")
    assert not is_valid_int_arg(" 1")
    assert not is_valid_int_arg("1a")
    assert not is_valid_int_arg("1111")
    assert not is_valid_int_arg("1111")
    assert not is_valid_int_arg("0111")