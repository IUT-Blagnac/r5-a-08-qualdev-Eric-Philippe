import time
from math import gcd
from functools import reduce

def parse(map: list[str]) -> dict[str, dict]:
    return {
        "L": {k: v[1:-1].split(", ")[0] for k, v in (line.split(" = ") for line in map)},
        "R": {k: v[1:-1].split(", ")[1] for k, v in (line.split(" = ") for line in map)}
    }


def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        instructions, seed, steps = [inst for inst in lines[0]], parse(lines[2:]), 0
        startNode = "AAA"

        while True:
            for i in instructions:
                startNode = seed["L" if i == "L" else "R"][startNode]
                steps += 1
                if startNode == "ZZZ":
                    return steps
                

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        instructions, seed, steps = [inst for inst in lines[0]], parse(lines[2:]), 0

        startNodes = set(node for node in seed["L"] if node.endswith("A"))
        endSteps = [0] * len(startNodes)

        for j, node in enumerate(startNodes):
            startNode = node
            steps = 0
            while True:
                for i in instructions:
                    startNode = seed["L" if i == "L" else "R"][startNode]
                    steps += 1
                    # if node ends with Z, we found a new end node
                    if startNode.endswith("Z"):
                        endSteps[j] = steps
                        break
                if endSteps[j] != 0:
                    break

        lcm = reduce(lambda x, y: x * y // gcd(x, y), endSteps)
        return lcm

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 8
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path_o = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input_o.txt"
    input_path_t = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input_t.txt"
    print("---Part One---")
    execute(part_one, input_path_o)

    print("---Part Two---")
    execute(part_two, input_path_t)