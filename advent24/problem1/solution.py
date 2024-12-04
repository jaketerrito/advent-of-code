# https://adventofcode.com/2024/day/1

import argparse
from heapq import heappop, heappush

# Given a file with two columns of integers seperated by whitespace
# Output a heap of the values for each column
# This isn't really necessary, just makes it possible to test the input parsing
def parse_column_file(file_name: str) -> tuple[list[int], list[int]]:
    heapA = []
    heapB = []
    with open(file_name) as file:
        for line in file.readlines():
            values = line.split()
            heappush(heapA, int(values[0]))
            heappush(heapB, int(values[1]))

    return heapA, heapB


def get_heap_corresponding_difference(heapA : list[int], heapB : list[int]) -> int:
    total_difference = 0
    for i in range(len(heapA)):
        total_difference += abs(heappop(heapA) - heappop(heapB))

    return total_difference


# Parse input into heaps
# Get difference between correspoding values in the heaps
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    heapA, heapB = parse_column_file(args.file_name)
    difference = get_heap_corresponding_difference(heapA, heapB)
    
    print(difference)
    


