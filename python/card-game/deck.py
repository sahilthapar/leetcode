from card import Card, CardColor, CardType
import random


class Deck:
    """
    Represents a whole deck of cards for a game as a list
    Should contain
        - 2 x 0-9 in each color = 80 cards
        - 2 x each action card in each color (skip, reverse, draw_two) = 24 cards
        - 4 x wild cards
        - 4 x wild_draw_four
    Methods
    - shuffle
    - draw a card
    - remaining cards
    - is deck empty
    """
    def __init__(self):
        self.cards = []
        self._create_deck()
        self.shuffle()

    def _create_deck(self):
        for color in CardColor:
            for n in range(10):
                self.cards.append(Card(card_type=CardType.NUMBER, color=color, value=n))
            for n in range(2):
                self.cards.append(Card(card_type=CardType.SKIP, color=color))
                self.cards.append(Card(card_type=CardType.REVERSE, color=color))
                self.cards.append(Card(card_type=CardType.DRAW_TWO, color=color))

        for n in range(4):
            self.cards.append(Card(card_type=CardType.WILD, color=None))
            self.cards.append(Card(card_type=CardType.WILD_DRAW_FOUR, color=None))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if not self.is_empty else None

    def cards_remaining(self):
        return len(self.cards)

    def is_empty(self):
        return self.cards_remaining() == 0