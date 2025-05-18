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
