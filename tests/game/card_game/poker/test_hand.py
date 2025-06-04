import collections

import pytest
from sportradar.game.card_game.poker.hand import Hand


class TestHand:
    def test_one_pair_score(self):
        hand = Hand({"K":"c", "K":"d" , "7":"c", "2":"s", "J":"h"})
        counts = hand.get_pair_card_score()
        assert counts == 2