from functools import cmp_to_key

card_values = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11, 
    'K': 12,
    'A': 13
}
sum = 0

class Hand:

    def __init__(self, hand, bet):
        self.hand = hand
        self.modded_hand = self.replaceJs()
        self.bet = int(bet)
        self.type = self.getType()

    def replaceJs(self):
        if 'J' not in self.hand: 
            return self.hand
        if self.hand == 'JJJJJ': 
            return 'AAAAA'
        count = {
            card: self.hand.count(card) for card in set(self.hand) - {'J'}
        }
        return self.hand.replace('J', sorted(count, key= lambda card: count[card])[-1])

    
    def getType(self):
        temp = sorted(self.modded_hand)
        if temp[0] == temp[1] and temp[1] == temp[2] and temp[2] == temp[3] and temp[3] == temp[4]:
            return 7
        elif (temp[0] == temp[1] and temp[1] == temp[2] and temp[2] == temp[3]) or (temp[1] == temp[2] and temp[2] == temp[3] and temp[3] == temp[4]):
            return 6
        elif (temp[0] == temp[1] and temp[1] == temp[2] and temp[3] == temp[4]) or (temp[0] == temp[1] and temp[2] == temp[3] and temp[3] == temp[4]):
            return 5
        elif (temp[0] == temp[1] and temp[1] == temp[2]) or (temp[1] == temp[2] and temp[2] == temp[3]) or  (temp[2] == temp[3] and temp[3] == temp[4]):
            return 4
        elif (temp[0] == temp[1] and temp[2] == temp[3]) or (temp[0] == temp[1] and temp[3] == temp[4]) or (temp[1] == temp[2] and temp[3] == temp[4]):
            return 3
        elif temp[0] == temp[1] or temp[1] == temp[2] or temp[2] == temp[3] or temp[3] == temp[4]:
            return 2
        else:
            return 1

def customSort(a, b):
    if a.type > b.type:
        return 1
    elif a.type < b.type:
        return -1
    else:
        for i in range(0, len(a.hand)):
            if card_values[a.hand[i]] > card_values[b.hand[i]]:
                return 1
            elif card_values[a.hand[i]] < card_values[b.hand[i]]:
                return -1
            else:
                continue
        return 0
    
cust_sort = cmp_to_key(customSort)

with open('day7/challenge7.txt', 'r') as file:
    lines = file.readlines()

hands = []

for line in lines:
    temp = line.split()
    hands.append(Hand(temp[0], temp[1]))

hands.sort(key = cust_sort)

for i in range(0, len(hands)):
    sum += (i+1) * hands[i].bet

print("Total winnings:", sum)