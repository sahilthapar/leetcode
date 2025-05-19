from typing import List
from game_state import GameState
from player import Player
from card import Card, CardType

class Game:
    """
    Represents a game of uno, with methods for possible actions and handling the effects of the card
    """
    def __init__(self, player_names: List[str]):
        self.game_state = GameState(player_names=player_names)
        self.game_over = False
        self.winner = None

    def can_play_card(self, player: Player, card_index: int) -> bool:
        if not 0 <= card_index < len(player.hand):
            return False

        played_card = player.hand[card_index]
        top_card = self.game_state.get_top_card()

        return played_card.can_play_on_top_of(top_card)

    def play_card(self, card_index: int) -> bool:
        current_player = self.game_state.get_current_player()
        if not self.can_play_card(player=current_player, card_index=card_index):
            return False

        # play the card
        played_card = current_player.play_card(card_index)
        self.game_state.discard_pile.append(played_card)

        # handle card effects


    def _handle_card_effects(self, card: Card):

        # skip the next player's turn
        if card.type == CardType.SKIP:
            self.game_state.next_player()

        elif card.type == CardType.REVERSE:
            self.game_state.reverse_direction()
            if len(self.game_state.players) == 2:
                self.game_state.next_player()

        # elif card.type == CardType.DRAW_TWO
