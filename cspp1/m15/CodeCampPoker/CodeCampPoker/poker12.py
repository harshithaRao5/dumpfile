'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
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
    for H in hand:
        face_values.append(card_values[H[0]])
    face_values.sort()
    for i in range(0, len(face_values)-1):
        if face_values[i+1] - face_values[i] != 1:
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
    for H in hand:
        if suit[1] != H[1]:
            return False
    return True
def four_of_a_kind(hand):
    face_value = []
    for H in hand:
        face_value.append(card_values[H[0]])
    face_value.sort()
    for i in range(0, len(face_value)-3):
        if face_value[i] == face_value[i+1] == face_value[i+2] == face_value[i+3]:
            return True
    return False
def three_of_a_kind(hand):
    face = []
    for H in hand:
        face.append(card_values[H[0]])
    face.sort()
    for i in range(0,len(face)-2):
        if face[i] == face[i+1] == face[i+2]:
            return True
    return False
def one_pair(hand):
    face1 = []
    for H in hand:
        face1.append(card_values[H[0]])
    face1.sort()
    for i in range(0,len(face1)-1):
        if face1[i] == face1[i+1]:
            return True
    return False
'''def full_house(hand):
    face_value1 = []
    for h in hand:
        face_value1.append(card_values[h[0]])
    face_value1.sort()
    for i in range(0, len(face_value1)-1):
        if face_value1[i] == face_value1[i+1] == face_value1[i+2] and face_value1[i+3] == face_value1[i+4]:
            return True
    return False'''
def two_pair(hand):
    face_value2 = []
    for H in hand:
        face_value2.append(card_values[H[0]])
    face_value2.sort()
    for i in range(0, len(face_value2)-1):
        if face_value2[i] == face_value2[i+1] and face_value2[i+2] == face_value2[i+3]:
            return True
    return False
def high_card(hand):
    face_value3 = []
    list1=[]
    for H in hand:
        face_value3.append(card_values[H[0]])
        list1=list(face_value3)
    lis1 = max(list1)    
    '''for i in range(0, len(face_value3)-1):
        if face_value3[i] == 14 or face_value3[i] == 13 or face_value3[i] == 12 or face_value3[i] == 11 or face_value3[i] == 10:
            return True
    return False'''
    
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 9
    if four_of_a_kind(hand):
        return 8
    if three_of_a_kind(hand):
        return 4
    if one_pair(hand):
        return 2
    if three_of_a_kind(hand) and one_pair(hand):
        return 7
    if two_pair(hand):
        return 3
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif high_card(hand):
        return lis1
    else:
        return 0
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
    return max(hands, key = hand_rank)
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
    