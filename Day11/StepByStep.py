import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card


def setup_cards():
    user_card = []
    computer_card = []

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    return user_card, computer_card


def calculate_score(list_of_cards):
    score = sum(list_of_cards)

    if len(list_of_cards) == 2 and score == 21:
        return 0

    if score > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return score





calculate_score(setup_cards())
