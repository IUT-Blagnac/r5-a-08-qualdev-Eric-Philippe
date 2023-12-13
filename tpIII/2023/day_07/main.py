import time

cardsDict = {
    "A": 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

rankType = {
    "HIGH CARD": 1,
    "ONE PAIR": 2,
    "TWO PAIRS": 3,
    "THREE OF A KIND": 4,
    "HOUSE": 5,
    "FOOR OF A KIND": 6,
    "QUINT FLUSH": 7
}

class Bet:
    def __init__(self, hand: str, bet: int):
        self.cards = [lettre for lettre in hand]
        self.bet = bet
        self.rank:int = self.determineHandRank()
        self.value:list[int] = [cardsDict[card] for card in self.cards]

    def __str__(self):
        return f"{self.cards} -> {self.rankToTxt()} -> {self.value} -> {self.bet}"
    
    def rankToTxt(self):
        for key, value in rankType.items():
            if value == self.rank:
                return key
    
    def determineHandRank(self):
        unique_cards = set(self.cards)
        counts = [self.cards.count(card) for card in unique_cards]

        if len(unique_cards) == 1:
            return 7
        elif 4 in counts:
            return 6
        elif 3 in counts:
            return 5 if len(unique_cards) == 2 else 4
        elif counts.count(2) == 2:
            return 3
        elif counts.count(2) == 1:
            return 2
        elif len(unique_cards) == 5:
            return 1

        
def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]

        bets = [Bet(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
        bets.sort(key=lambda x: (x.rank, x.value))

        
        total = sum(bet.bet * (i + 1) for i, bet in enumerate(bets))

        return total
    
cardsDict.update({'J': 0})

class SuperBet(Bet):
    def determineHandRank(self):
        cards = [card for card in self.cards if card != 'J']
        unique_cards = set(cards)
        counts = [cards.count(card) for card in unique_cards]
        jokerCount = self.cards.count('J')
        hasJoker = 'J' in self.cards

        if len(set(self.cards)) == 1:
            return 7
        
        if 4 in counts:
            return 7 if hasJoker else 6
        
        if 3 in counts:
            if jokerCount == 2:
                return 7
            return 6 if jokerCount == 1 else 5 if len(unique_cards) == 2 else 4
        
        if sum(count == 2 for count in counts) == 2:
            return 5 if hasJoker else 3

        if sum(count == 2 for count in counts) == 1:
            return 7 if jokerCount == 3 else 6 if jokerCount == 2 else 4 if jokerCount == 1 else 2
        
        return 7 if jokerCount == 4 else 6 if jokerCount == 3 else 4 if jokerCount == 2 else 2 if jokerCount == 1 else 1

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        lines: list[str] = [line.strip() for line in lines]

        bets = [SuperBet(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
        bets.sort(key=lambda x: (x.rank, x.value))

        
        total = sum(bet.bet * (i + 1) for i, bet in enumerate(bets))

        return total
    
def execute(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    print(result)
    print(f"Temps d'exécution : {execution_time_ms:.3f} ms")

if __name__ == "__main__":
    YEAR = 2023
    DAY = 7
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    execute(part_one, input_path)

    print("---Part Two---")
    execute(part_two, input_path)