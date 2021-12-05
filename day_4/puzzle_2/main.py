import functools
from pprint import pprint
from typing import List

def read_input():
    with open("input.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())
        
    return lines

data = read_input()

class Card:
    line_length = 5
    
    def __init__(self, numbers):
        self.numbers = numbers

    def check_new_number(self, number):
        for row in self.numbers:
            if number in row:
                return True
        return False

    def check_if_completed(self, numbers_drawn):
        for row in self.numbers:
            if all([x in numbers_drawn for x in row]):
                return True
        for i in range(self.line_length):
            if all([row[i] in numbers_drawn for row in self.numbers]):
                return True
        return False

    def calculate_result(self, numbers_drawn, final_number):
        not_drawn_sum = 0
        for row in self.numbers:
            for number in row:
                if number not in numbers_drawn:
                    not_drawn_sum += number
        return not_drawn_sum * final_number


card_numbers = []
all_cards: List[Card] = []
first_line = True

for line in data:
    if line == "":
        all_cards.append(Card(card_numbers))
        card_numbers = []
        continue
    if first_line:
        numbers_to_draw = [int(c) for c in line.split(",")]
        first_line = False
        continue

    card_numbers.append([int(c) for c in line.split()])

numbers_drawn = []
result_found = False

for number in numbers_to_draw:
    if result_found:
        break

    cards_not_completed = []

    numbers_drawn.append(number)
    for card in all_cards:
        if not card.check_new_number(number):
            cards_not_completed.append(card)
            continue
        if not card.check_if_completed(numbers_drawn):
            cards_not_completed.append(card)
            continue

    if len(cards_not_completed) == 1:
        result = card.calculate_result(numbers_drawn, number)
        result_found = True
        break
    
    all_cards = cards_not_completed

print(result)
