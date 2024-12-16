import argparse
from typing import Optional


def get_diagnols(puzzle: list[list], backwards: Optional[bool] = False) -> list[list]:
    first_column =  {(row, 0) for row in range(len(puzzle))}
    first_row = {(0, col) for col in range(len(puzzle[0]))}
    diagonal_starting_points = first_column | first_row
    diagnols = []
    if backwards:
        puzzle = puzzle[::-1]

    for row, col in diagonal_starting_points:
        diagnol =[]
        while row < len(puzzle) and col < len(puzzle[0]):
            diagnol.append(puzzle[row][col])
            row += 1
            col += 1
        diagnols.append(diagnol)

    return diagnols


def get_count(lines: list[list], word: Optional[str] = "XMAS") -> int:
    count = 0
    for line in lines:
        line = ''.join(line)
        count += line.count(word)
        count += line.count(word[::-1])

    return count


def word_count(puzzle: str) -> int:
    rows = puzzle.split("\n")

    num_columns = len(rows[0])
    columns = [[row[i] for row in rows] for i in range(num_columns)]

    diagnols_right = get_diagnols(rows)
    diagnols_left = get_diagnols(rows, True)

    return get_count(diagnols_left) + get_count(diagnols_right) + get_count(rows) + get_count(columns)

def xmas_count(puzzle: str) -> int:
    puzzle = puzzle.split("\n")
    count = 0
    for row_index in range(1,len(puzzle)-1):
        for col_index in range(1, len(puzzle)-1):
            if puzzle[row_index][col_index] == 'A':
                top_left_diag = {puzzle[row_index-1][col_index-1], puzzle[row_index+1][col_index+1]}
                bot_left_diag = {puzzle[row_index+1][col_index-1], puzzle[row_index-1][col_index+1]}
                if top_left_diag == {'M','S'} and bot_left_diag ==  {'M', 'S'}:
                    count += 1

    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    with open(args.file_name) as file:
        puzzle = file.read().strip()
        print(f'count xmas: {word_count(puzzle)}')

        print(f'count x-mas: {xmas_count(puzzle)}')