from typing import List
from card import Card


class Player:
    """
    Represents a player in the game
    Properties
    - name
    - hand of cards

    Actions
    - draw a card
    - play a card
    - find playable cards
    """

    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_card(self, card: Card):
        self.hand.append(card)

    def play_card(self, idx: int) -> Card:
        """
        Represents playing a card in the game
        :param idx: index of card to be played in the hand
        :return:
        """
        # check whether idx is valid
        if 0 <= idx < len(self.hand):
            return self.hand.pop(idx)
        raise IndexError("Invalid card index")

    def find_playing_cards(self, top_card: Card) -> List[int]:
        """
        Find all indices of cards that can be played on top of the current top_card
        :param top_card:
        :return:
        """
        playable = []
        for i, card in enumerate(self.hand):
            if card.can_play_on_top_of(top_card):
                playable.append(i)
        return playable

