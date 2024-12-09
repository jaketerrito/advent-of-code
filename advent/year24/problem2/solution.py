import argparse
from typing import Optional

# Given a file where each line is a list of integers seperated by spaces (a report)
# Output a list of these lists (reports)
def parse_reports(file_name: str) -> list[list[int]]:
    reports = []

    with open(file_name) as file:
        for line in file.readlines():
            reports.append([int(x) for x in line.split(' ')])

    return reports


# A report is safe if:
# - the values are either all increasing or all decreasing
# - adjacent values don't differ by atleast 1 and no more than 3
def is_report_safe(report: list[int], dampen: Optional[bool] = False) -> bool:
    decreasing = report[0] > report[1]
    
    for i in range(0, len(report)-1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3 or (decreasing != (report[i] > report[i+1])):
            if dampen:
                for j in range(max(0, i-1), min(len(report), i+2)):
                    dampened_report = [value for index, value in enumerate(report) if index != j]
                    print(dampened_report)
                    if is_report_safe(dampened_report):
                        return True
            return False
        
    return True

# Get the total count of safe reports from a list of reports
def count_safe_reports(reports: list[list[int]], dampened : Optional[bool] = False) -> int:
    return sum([is_report_safe(report, dampened) for report in reports])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    reports = parse_reports(args.file_name)
    
    safe_reports = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_reports}")

    safe_reports_dampened = count_safe_reports(reports, True)
    print(f"Number of safe reports with dampener: {safe_reports_dampened}")