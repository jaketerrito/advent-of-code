import argparse

def is_valid_int_arg(arg: str) -> bool:
    if len(arg) > 3:
        return False
    if len(arg) < 1:
        return False
    
    return all(char.isnumeric() for char in arg)


def sum_corrupted_mul_instructions(instructions: str) -> int:
    total = 0
    chunks = instructions.split('mul(')

    # If mul command was not found
    if len(chunks) == 1:
        return total
    
    for chunk in chunks:
        comma = chunk.find(',')
        paren = chunk.find(')')

        # if comma or paren don't exist, or paren comes before comma
        if comma == -1 or paren == -1 or comma >= paren:
            continue
        
        first_arg = chunk[:comma]
        second_arg = chunk[comma + 1: paren]

        if not is_valid_int_arg(first_arg) or not is_valid_int_arg(second_arg): 
            continue

        first_int = int(first_arg)
        second_int = int(second_arg)

        total += first_int * second_int
    return total

def do_dont_sum_corrupted_mul_instructions(instructions: str) -> int:
    total = 0
    donts_chunks = instructions.split('don\'t()')

    total += sum_corrupted_mul_instructions(donts_chunks[0])

    for chunk in donts_chunks:
        total += sum(sum_corrupted_mul_instructions(do) for do in chunk.split("do()")[1:])

    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    with open(args.file_name) as file:
        data = file.read()
        total = sum_corrupted_mul_instructions(data)
        print(f"total: {total}")

        do_dont_total = do_dont_sum_corrupted_mul_instructions(data)
        print(f"do_dont_total: {do_dont_total}")
