file = open("7a_real.txt")
file_lines = file.readlines()

score_dict = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8,
              "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}
score_4 = {16: 25, 10: 17, 8: 13, 6: 11, 4: 7}
score_3 = {9: 25, 5: 17, 3: 11}
score_2 = {4: 25, 2: 17}


class Hand:
    def __init__(self, input_string):
        self.cards = input_string.strip().split(" ")[0]
        self.bid = int(input_string.strip().split(" ")[1])
        self.strength = 0
        self.non_J_cards = list(filter("J".__ne__, self.cards))
        for c in enumerate(self.non_J_cards):
            self.strength += self.non_J_cards.count(c[1])  # main score
        if len(self.non_J_cards) == 4:  # update for Jokers
            self.strength = score_4[self.strength]
        elif len(self.non_J_cards) == 3:
            self.strength = score_3[self.strength]
        elif len(self.non_J_cards) == 2:
            self.strength = score_2[self.strength]
        elif len(self.non_J_cards) in (1, 0):
            self.strength = 25
        for c in enumerate(self.cards):
            self.strength += score_dict[c[1]] * 10 ** ((c[0]+1) * -2)  # high card score


def hand_sort_key(hand):  # a key to sort the list of hands
    return hand.strength


hands = []
for line in file_lines:  # load the input
    hands.append(Hand(line))

hands.sort(key=hand_sort_key)  # sort them by strength

ans = 0
for h in enumerate(hands):
    ans += h[1].bid * (h[0]+1)  # rank and calc winnings then

print(ans)
