import math as m, re
import time

def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        
        return sum(sum(p) for p in attribute_value_to_char(lines).values())

"""
Retourne un dictionnaire de la forme {(r, c): [v1, v2, ...], ...} où (r, c) est la position d'un caractère 
et [v1, v2, ...] est la liste des valeurs des nombres voisins de ce caractère.
"""
def attribute_value_to_char(lines: list[str]) -> dict[str, list[int]]:

    lineLength = len(lines[0])
    notSymbol = set('0123456789.')
    chars = {(r, c): [] for r in range(lineLength) for c in range(lineLength) if lines[r][c] not in notSymbol}
    # Parcourir chaque ligne du tableau
    for r, row in enumerate(lines):
        # Utiliser une expression régulière pour trouver tous les nombres dans la ligne
        # Match les nombres de 1 ou plusieurs chiffres
        int_enumerator = re.finditer(r'\d+', row)
        for n in int_enumerator:
            # Créer un ensemble de positions voisines du nombre trouvé
            neighbourPos = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}
            # Ajouter le nombre trouvé à la liste correspondante dans le dictionnaire chars
            for foundNum in neighbourPos & chars.keys():
                chars[foundNum].append(int(n.group()))
    return chars

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]
        
        return sum(m.prod(p) for p in attribute_value_to_char(lines).values() if len(p) == 2)

def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 3
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)