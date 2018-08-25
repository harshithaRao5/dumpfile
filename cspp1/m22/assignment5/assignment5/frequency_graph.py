'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''freq = {}
    for x in dictionary:
        freq[x] = freq.get(x,0) + '#'
    return freq
    keys = sorted(dictionary.keys())
    for key in keys:
        print(key, "-", dictionary[key])'''
    keys = sorted(dictionary.keys())
    for key in keys:
    	value = dictionary[key].get(key, 0) + '#'
    	print(key, "-", value)



def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
