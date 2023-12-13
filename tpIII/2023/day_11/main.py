import time

def part_one(file_name: str) -> int:
    with open(file_name) as f:
        data = f.read().splitlines()
        grid = {(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "#"}
        horizontal = set(range(len(data[0]))) - {x for x, y in grid}
        vertical = set(range(len(data))) - {y for x, y in grid}
        s, s2 = 0, 0
        for galaxy in set(grid):
            grid.remove(galaxy)
            for other_galaxy in grid:
                left_h, right_h = sorted([galaxy[0], other_galaxy[0]])
                left_v, right_v = sorted([galaxy[1], other_galaxy[1]])
                sum_dist = right_h - left_h + right_v - left_v
                extra_h = sum(1 for x in horizontal if left_h < x < right_h)
                extra_v = sum(1 for x in vertical if left_v < x < right_v)
                s += sum_dist + (sum_extra := extra_h + extra_v)
                
        return s
    
def part_two(file_name: str) -> int:
    with open(file_name) as f:
        data = f.read().splitlines()
        grid = {(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "#"}
        horizontal = set(range(len(data[0]))) - {x for x, y in grid}
        vertical = set(range(len(data))) - {y for x, y in grid}
        s, s2 = 0, 0
        for galaxy in set(grid):
            grid.remove(galaxy)
            for other_galaxy in grid:
                left_h, right_h = sorted([galaxy[0], other_galaxy[0]])
                left_v, right_v = sorted([galaxy[1], other_galaxy[1]])
                sum_dist = right_h - left_h + right_v - left_v
                extra_h = sum(1 for x in horizontal if left_h < x < right_h)
                extra_v = sum(1 for x in vertical if left_v < x < right_v)
                s += sum_dist + (sum_extra := extra_h + extra_v)
                s2 += sum_dist + sum_extra * 999999

        return s2
    
def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 11
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)