import argparse


# Rules is a dict with key as page and value being list of pages that can't come after that page
def get_rules_and_updates(data: list[str]) -> tuple[dict, list]:
    rules = {}
    updates = []
    split_index = data.index('')
    for line in data[:split_index]:
        rule_params = line.split('|')
        first = rule_params[0]
        second = rule_params[1]
        rule = rules.get(second, set())
        rule.add(first)
        rules[second] = rule

    updates = [line.split(',') for line in data[split_index+1:]]

    return rules, updates

# assuming that pages are not repeated
def correct_update(rules: dict, update: list) -> list:
    update = update.copy()

    i = 0
    while i < len(update) -1:
        out_of_order_pages = set(update[i+1:]) & rules.get(update[i], set())
        if out_of_order_pages:
            for page in out_of_order_pages:
                bad_page_index = update.index(page)
                update.pop(bad_page_index)
                update.insert(i, page)
        else:
            i += 1
    return update



def is_update_correct(rules: dict, update: list) -> bool:
    seen  = set()
    # Rules tell us which pages can't come after a given page
    # So iterate backwards and check that rule is satisfied
    for page in update[::-1]:
        if page in rules and rules[page] & seen:
            return False
        seen.add(page)

    return True

def get_middle_page_number(update: list) -> int:
    return int(update[len(update) // 2])
        

def get_solution(data: list[str]) -> int:
    rules, updates = get_rules_and_updates(data)

    total = 0
    for update in updates:
        if is_update_correct(rules, update):
            total += get_middle_page_number(update)

    return total

def get_incorrect_solution(data: list[str]) -> int:
    rules, updates = get_rules_and_updates(data)

    total = 0
    for update in updates:
        if not is_update_correct(rules, update):
            corrected = correct_update(rules, update)
            total += get_middle_page_number(corrected)

    return total
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    with open(args.file_name) as file:
        lines = file.read().splitlines()
        print(get_solution(lines))
        print(get_incorrect_solution(lines))
