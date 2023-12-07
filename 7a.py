file = open("7a_real.txt")
file_lines = file.readlines()

score_dict = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7,
              "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}


class Hand:
    def __init__(self, input_string):
        self.cards = input_string.strip().split(" ")[0]
        self.bid = int(input_string.strip().split(" ")[1])
        self.strength = 0
        for c in enumerate(self.cards):
            self.strength += self.cards.count(c[1])  # main score
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
