class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        # sort
        deck.sort() 

        def organize(deck):
            if len(deck) == 1:
                return deck
            mid = (len(deck) + 1)// 2
            first = deck[:mid]
            second = organize(deck[mid:])
            newDeck  = []

            if len(first) > len(second):
                second.insert(0, second.pop())

            for a,b in zip(first, second):
                newDeck.append(a)
                newDeck.append(b)
            if len(first) > len(second):
                newDeck.append(first[-1])
            return newDeck

        return organize(deck)

        # save first half
        # get second half
        #   
        # 2 3 5 7 11 13 17
        # 11 13 17
        # 17


        # 13,11,17
        # 17,10,13, 11
        # 19,13,21,17,20

        # 1 2 3 4 5 

        # 5 6, 7
        # 6 5 7

        # 6, 7] [8, 9
        # 9 6 8 7

        # 6 8 7 9

        # 1 9  2 

        # 5 7 6
        #  