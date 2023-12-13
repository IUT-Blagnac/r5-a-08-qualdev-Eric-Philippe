import time
import re
from typing import List
from functools import reduce

# def part_one(file_name: str) -> int:
#     with open(file_name) as f:
#         lines = f.readlines()
#         lines: list[str] = [line.strip() for line in lines]
#         data = [re.findall(r'\d+', line) for line in lines]
#         racesLength: list[int] = data[0]
#         records: list[int] = data[1]
#         possibilities: list[int] = [0] * len(racesLength)
#         print(possibilities)

#         for i in range(len(racesLength)):
#             raceLength = int(racesLength[i])
#             record = int(records[i])
#             for x in range(raceLength):
#                 race_result = (raceLength - x) * x
#                 if (race_result > record):
#                     possibilities[i] += 1

#         return reduce(lambda x, y: x * y, possibilities)

def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines: List[str] = [line.strip() for line in f.readlines()]

        racesLength, records = [list(map(int, re.findall(r'\d+', line))) for line in lines[:2]]

        possibilities = [sum((raceLength - x) * x > record for x in range(raceLength)) for raceLength, record in zip(racesLength, records)]

        return reduce(lambda x, y: x * y, possibilities)

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        data = [re.findall(r'\d+', line) for line in lines]
        timeTotal = int(''.join(map(str, data[0])))
        recordTotal = int(''.join(map(str, data[1])))

        a = -1 
        b = int(timeTotal)
        c = -1*int(recordTotal)
        d = b*b - (4*a*c)
        x1, x2 = int((-b + d**0.5)/(2*a)), int(((-b - d**0.5)/(2*a)))

        return x2 - x1
    
def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 6
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)