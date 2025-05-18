import typing
from enum import Enum
from typing import Optional

class CardColor(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    BLUE = 'blue'
    GREEN = 'green'

class CardType(Enum):
    NUMBER = 'number'
    SKIP = 'skip'
    REVERSE = 'reverse'
    DRAW_TWO = 'draw_two'
    WILD = 'wild'
    WILD_DRAW_FOUR = 'wild_draw_four'

class Card:
    """
    Represents a single card in the game
    Properties of a card
    - card-color
    - card-type
    - card-value (number if type is numeric)
    """
    def __init__(self, card_type: CardType, color: Optional[CardColor], value: Optional[int] = None):
        self.type = card_type
        self.color = color
        self.value = value

    def is_wild(self):
        """
        Checks if card_type is wild
        :return:
        """
        return self.type in [CardType.WILD, CardType.WILD_DRAW_FOUR]

    def can_play_on_top_of(self, other_card: typing.Self, chosen_color: Optional[CardColor] = None) -> bool:
        """
        Checks if this card can be played on top of the "other_card"
        - if wild, return true, can always be played
        - if other_card is wild, just match chosen color
        - else
            - check if color matches
        :param other_card:
        :param chosen_color:
        :return:
        """
        if self.is_wild():
            return True

        if other_card.is_wild() and self.color == chosen_color:
            return True

        if self.color == other_card.color:
            return True

        if self.type == other_card.type == CardType.NUMBER and self.value == other_card.value:
            return True

        if self.type == other_card.type != CardType.NUMBER:
            return True

        return False


