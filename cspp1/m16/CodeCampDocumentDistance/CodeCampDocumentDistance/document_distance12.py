'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
FILE_NAME = "stopwords.txt"
def clean_up(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower()
    input1=[reg.sub('',w.strip())for w in input1.split(' ')]

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    
def create_dictionary(input1.input2):
    d={}
    d=load_stopwords(stopwords)
    wordlist1=clean_up(input1)
    wordlist2=clean_up(input2)
    wordlist=wordlist2+wordlist2
    d1={}
    for word in wordlist:
        if word not in d:
            if word not in d1:
                d1[word]=(wordlist1.count(word),wordlist2.count(word))



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
    input1 = input().lower()
    input2 = input().lower()
    print(similarity(input1, input2))
if __name__ == '__main__':
    main()
