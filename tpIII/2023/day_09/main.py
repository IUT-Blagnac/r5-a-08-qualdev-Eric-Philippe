import time

def process(line: list[int]) -> list[list[int]]:
    tableaux_finaux = [line]
    while any(tableaux_finaux[-1]):
        tableau_suivant = [b - a for a, b in zip(tableaux_finaux[-1], tableaux_finaux[-1][1:])]
        tableaux_finaux.append(tableau_suivant)

    return tableaux_finaux

def predicate_future(table: list[list[int]]) -> int:
    table[-1].append(table[-1][-1])
    for i in range(len(table) - 2, -1, -1):
        lastValueCurTableau = table[i][-1]
        lastValuePrevTableau = table[i + 1][-1]
        table[i].append(lastValueCurTableau + lastValuePrevTableau)

    return table[0][-1]

def predicate_past(table: list[list[int]]) -> int:
    table[-1].insert(0, table[-1][0])
    for i in range(len(table) - 2, -1, -1):
        lastValueCurTableau = table[i][0]
        lastValuePrevTableau = table[i + 1][0]
        table[i].insert(0, lastValueCurTableau - lastValuePrevTableau)

    return table[0][0]


def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        lines: list[list[int]] = [[int(number) for number in line.split()] for line in lines]

    return sum(predicate_future(process(line)) for line in lines)

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        lines: list[list[int]] = [[int(number) for number in line.split()] for line in lines]

    return sum(predicate_past(process(line)) for line in lines)

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 9
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)