import time

def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]

        total = 0
        for line in lines:
            left = list(map(int, line.split("|")[0].split(": ")[1].split()))
            right = list(map(int, line.split("|")[1].split()))

            res = checkCard(left, right)
            total += 0 if res == 0 else 2 ** (res - 1)
        return total

"""
Using set for performance
"""
def checkCard(leftNumbers: list[int], rightNumbers: list[int]) -> int:
    return len(set(leftNumbers).intersection(rightNumbers))

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        # Describe the amount of match in the card {game: amount of matching numbers}
        dictGames: dict[int, int] = {}
        for i, line in enumerate(lines):
            # Parse the left and right numbers
            left = list(map(int, line.split("|")[0].split(": ")[1].split()))
            right = list(map(int, line.split("|")[1].split()))

            # Count the number of matching numbers
            matchingAmount = checkCard(left, right)
            dictGames[i] = matchingAmount

        # Describe the amount of cards including the copied cards
        dictListGames: dict[int, int] = [1] * len(dictGames)

        for i, game in enumerate(dictGames):
            increment = dictListGames[i]
            if increment > 0:
                end_index = i + dictGames[game] + 1
                dictListGames[i + 1:end_index] = [count + increment for count in dictListGames[i + 1:end_index]]


        totalScratchCards = sum(dictListGames)

        
    return totalScratchCards

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 4
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)