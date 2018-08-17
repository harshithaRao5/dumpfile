'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE_NAME = "stopwords.txt"
def clean_up(input1):
    reg = re.compile('^[a-z]')
    input1 = input1.lower()
    for i in input1.split(''):
        if i in reg:
            print(i)




def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
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
