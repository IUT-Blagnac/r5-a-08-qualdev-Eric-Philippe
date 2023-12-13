import time

# We're gonna work in a [RGB] order [Red Score, Green Score, Blue Score]
# [12, 13, 14] means that the red cube as a score of 12, the green cube as a score of 13 and the blue cube as a score of 14
def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        #              R   G   B
        MAX_VALUES = [12, 13, 14]

        valid_games = 0
        for line in lines:
            game = parser(line)
            scores = get_maximum_cube_count(game)
            for i in range(len(scores)):
                if scores[i] > MAX_VALUES[i]:
                    break
            else:
                game_id = line.split(": ")[0].split(" ")[1].strip()
                i_game = int(game_id)
                valid_games += i_game

        return valid_games
                    

def parser(line: str) -> list[list[str]]:
    final_list = []
    sets = line.split(": ")[1].split("\n")[0]
    final_list = [s.split(", ") for s in sets.split(";")]
    final_list = [[value.strip() for value in s] for s in final_list]

    return final_list

def get_maximum_cube_count(sets: list[list[str]]) -> list[int]:
    color_indices = {'red': 0, 'green': 1, 'blue': 2}
    scores = [0, 0, 0]

    for s in sets:
        for value in s:
            temp_score, color = map(str.strip, value.split(" "))
            color_index = color_indices[color]
            scores[color_index] = max(scores[color_index], int(temp_score))

    return scores


def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()

        valid_games = 0
        for line in lines:
            game = parser(line)
            scores = get_maximum_cube_count(game)
            scores_multiplied = scores[0] * scores[1] * scores[2]
            valid_games += scores_multiplied

        return valid_games

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 2
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)
    