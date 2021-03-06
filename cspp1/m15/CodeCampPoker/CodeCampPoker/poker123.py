'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
CARD_VALUES = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    face_values = []
    for h_1 in hand:
        face_values.append(CARD_VALUES[h_1[0]])
    face_values.sort()
    i = 0
    for i in range(0, len(face_values)-1):
        if face_values[i+1]-face_values[i] != 1:
            return False
    return True


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit = hand[0]
    for h_1 in hand:
        if suit[1] != h_1[1]:
            return False
    return True
def card_ranks(hand):
    '''returns the max rank'''
    ranks = sorted(['--23456789TJQKA'.index(c) for c, s in hand])
    ranks.reverse()
    return ranks
def kind(ranks, n_1):
    '''returns whether one or three or four are of same kind'''
    for r_1 in ranks:
        if ranks.count(r_1) == n_1:
            return r_1
    return 0
def two_pair(ranks):
    '''checks two pairs are equal or not'''
    one_1 = kind(ranks, 2)
    two_2 = kind(sorted(ranks), 2)
    if one_1 and two_2:
        return (one_1, two_2)
    return None
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    ranks = card_ranks(hand)
    if is_straight(hand) and is_flush(hand):
        return(8, ranks)
    if kind(ranks, 4):
        return(7, kind(ranks, 4), ranks)
    if kind(ranks, 3) and kind(ranks, 2):
        return(6, (kind(ranks, 3), kind(ranks, 2)))
    if is_flush(hand):
        return(5, ranks)
    if is_straight(hand):
        return(4, ranks)
    if kind(ranks, 3):
        return(3, kind(ranks, 3), ranks)
    if two_pair(ranks):
        return(2, two_pair(ranks), ranks)
    if kind(ranks, 2):
        return(1, kind(ranks, 2), ranks)
    return(0, ranks)
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    