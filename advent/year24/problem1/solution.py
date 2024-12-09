# https://adventofcode.com/2024/day/1

import argparse
from heapq import heapify, heappop, heappush

# Given a file with two columns of integers seperated by whitespace
# Output a list of values for each column
def parse_column_file(file_name: str) -> tuple[list[int], list[int]]:
    listA = []
    listB = []
    with open(file_name) as file:
        for line in file.readlines():
            values = line.split()
            listA.append(int(values[0]))
            listB.append(int(values[1]))

    return listA, listB


def get_list_corresponding_difference(listA : list[int], listB : list[int]) -> int:
    listA = sorted(listA)
    listB = sorted(listB)

    total_difference = 0
    for a, b in zip(listA, listB):
        total_difference += abs(a - b)

    return total_difference

def get_counts(list: list[int]) -> dict[int, int]:
    counts = {}
    for x in list:
        counts[x] = counts.get(x, 0) + 1
    return counts

def get_similarity_score(listA: list[int], listB : list[int]) -> int:
    countsA = get_counts(listA)
    countsB = get_counts(listB)

    score = 0
    for key, countA in countsA.items():
        score += key * countA * countsB.get(key, 0)

    return score


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    listA, listB = parse_column_file(args.file_name)

    difference = get_list_corresponding_difference(listA, listB)
    print(f'Difference score: {difference}')

    similarity = get_similarity_score(listA, listB)    
    print(f'Similarity score: {similarity}')
    


