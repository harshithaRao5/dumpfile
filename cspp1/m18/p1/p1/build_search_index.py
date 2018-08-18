'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
file_name = "stopwords.txt"
import re
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    reg = re.compile('[^a-z]')
    text = [reg.sub('',w.strip()) for w in text]
    return text

def build_search_index(docs):
    

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    clean_input = word_list(docs)
    adict={}
    if docs.count('\n') > 1:
        inp_1 = docs.split("\n")
        inp_1 = inp_1[:len(inp_1)-1]
        for words in clean_input:
            if words not in load_stopwords(file_name).keys():
                for (i, j) in enumerate(inp_1):
                    if inp-1[i][0] not in adict:
                        adict[inp_1[i][0]] = inp_1[i][1].count(word)
                    else:
                        adict[inp_1[i][0]].append(inp_1[i][1].count(word))
    return adict

'''adict = {}
    if data.count('\n') > 1:
        inp_1 = data.split("\n")
        inp_1 = inp_1[:len(inp_1)-1]

        for (i, j) in enumerate(inp_1):
            inp_1[i] = j.split(" follows ")
            # print(inp_1[i][0])
            if inp_1[i][0] not in adict:
                adict[inp_1[i][0]] = inp_1[i][1].split(',')
            else:
                adict[inp_1[i][0]].extend(inp_1[i][1].split(','))
        return adict
    return adict'''




# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))
    
if __name__ == '__main__':
    main()
