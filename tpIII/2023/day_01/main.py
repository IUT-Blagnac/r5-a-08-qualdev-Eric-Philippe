import time

def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        total_sum = 0
        first_int = None # 5
        last_int = None # 2
        for line in lines:
            # Parcourir chaque caractère de la ligne
            for char in line:
                if char.isdigit():
                    if first_int == None:
                        first_int = int(char)
                    else:
                        last_int = int(char)
            # Put the two digits next to each other
            if last_int == None:
                last_int = first_int
            if first_int != None and last_int != None:
                    total_sum += first_int * 10 + last_int
                    first_int = None
                    last_int = None

    return total_sum

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        nums = [(1, '1', 'one'),
                (2, '2', 'two'),
                (3, '3', 'three'),
                (4, '4', 'four'),
                (5, '5', 'five'),
                (6, '6', 'six'),
                (7, '7', 'seven'),
                (8, '8', 'eight'),
                (9, '9', 'nine')]

        total = 0
        for line in lines:
            index = []
            for num in nums:
                try:
                    # Find the first occurence of the digit
                    i = line.index(num[1])
                    index.append((num[0], i))

                    # Find the last occurence of the digit
                    i = line.rindex(num[1])
                    index.append((num[0], i))

                except ValueError:
                    pass

                try:
                    i = line.index(num[2])
                    index.append((num[0], i))

                    i = line.rindex(num[2])
                    index.append((num[0], i))
                except ValueError:
                    pass

            total += index[0][0] * 10 + index[-1][0]

    return total

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    input_path = "./2023/day_01/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)