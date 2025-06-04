import collections

IS_HIGH_CARD = 0
IS_PAIR = 1
IS_TWO_PAIR = 2

class Hand:



    def __init__(self, inp_cards:dict):
        '''

        :param inp_cards:
        '''
        self.__cards = inp_cards
        self._scoring_strategies = [IS_HIGH_CARD,IS_PAIR,IS_TWO_PAIR]

    def get_cards(self)->dict:
        return self.__cards

    def get_score(self)->int:
        for strategy in self._scoring_strategies:
            if strategy == IS_HIGH_CARD:
                if self.__is_high_card():
                    return self.__get_high_card_score()
            elif strategy == IS_PAIR:
                if not self.__is_pair() and not self.__is_two_pirs():
                    return self.get_pair_card_score()
            elif strategy == IS_TWO_PAIR:
                if self.__is_two_pirs():
                    return self.__get_two_pair_card_score()


    def __is_high_card(self)->bool:
        pass


    def __get_high_card_score(self)->int:
        return 1

    def __is_pair(self)->bool:
        pass

    def get_pair_card_score(self)->int:
        counts:dict = collections.Counter(self.__cards)
        for (key,value) in counts.items():
            if value == 2:
                return 2
        return 0



    def __is_two_pirs(self)->bool:
        pass

    def __get_two_pair_card_score(self)->int:
        pass

if __name__ == "__main__":
    hand = Hand({"K":"c", "K":"d" , "7":"c", "2":"s", "J":"h"})
    hand.get_pair_card_score()

