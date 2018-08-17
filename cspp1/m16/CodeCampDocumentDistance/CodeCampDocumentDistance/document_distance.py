'''
    Document Distance - A detailed description is given in the PDF
'''
import math
file_name = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    '''for i in dict1:
        if i not in '!@#$%^&*()':
            list1 = i +  list1'''
    word_list1 = dict1.split()
    word_list2 = dict2.split()
    word_list3 = word_list1 + word_list2
    dict3={}
    for word in word_list3:
        if word not in load_stopwords(file_name).keys() and '!@#$%^&*()_-+}{:"<>?[];,.1234567890' and "'" :
            dict3[word] = (word_list1.count(word),word_list2.count(word))
    numerator = 0
    denominator = 0
    sum_1 = 0
    sum_2 = 0
    for i in dict3:
        numerator = numerator + dict3[i][0]*dict3[i][1]
        sum_1 = dict3[i][0]^2
        sum_2 = dict3[i][1]^2
        denominator = math.sqrt(sum1)*math.sqrt(sum2)
    return (numerator/denominator)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input1.lower()
    input2 = input()
    input2.lower()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
