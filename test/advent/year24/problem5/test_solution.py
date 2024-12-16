from advent.year24.problem5.solution import correct_update, get_incorrect_solution, get_middle_page_number, get_rules_and_updates, get_solution, is_update_correct


def test_rules_and_updates():
    data = [
        '1|2',
        '1|3',
        '4|2',
        '',
        '1,2,3',
        '3,2,1'
    ]
    rules, updates = get_rules_and_updates(data)
    assert rules == {'2': {'1', '4'}, '3': {'1'}}
    assert updates == [['1', '2', '3'], ['3', '2', '1']]


def test_correct_update():
    rules = {'4': {'3','2','1'}}
    
    assert ['3','4'] == correct_update(rules, ['4','3'])

def test_is_update_correct():
    rules = {'4': {'3','2','1'}}

    assert is_update_correct(rules, ['4'])
    assert is_update_correct(rules, ['1','2','3','4'])
    assert not is_update_correct(rules, ['4','3'])


def test_get_middle_page_number():
    assert get_middle_page_number("75,47,61,53,29".split(',')) == 61
    assert get_middle_page_number("97,61,53,29,13".split(',')) == 53
    assert get_middle_page_number("75,29,13".split(',')) == 29


def test_example():
    input = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

    assert get_solution(input.split('\n')) == 143

    assert get_incorrect_solution(input.split('\n')) == 123