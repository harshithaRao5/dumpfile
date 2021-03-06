'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the passfollows below and start writing your code
    '''data={}
    for key, value in data.items():
        data[key]=value.split("follows")
        if data[key] not in data:
            data[key]=[value]
        elif value not in data[key]:
            data[key].append(value)
    print(data[key,value])'''
    '''data={}
    for i in range(lines):
        res=data.split("follows")
        if res[i] not in data:
            data[res[i]]=[res[i+1]]
        else:
            if res[i+1] not in data[res[0]]:
                data[res[i]].append(data[res[i+1]])
    print(data)'''
    if data.count('\n') > 1:
        inp_1 = data.split("\n")
        inp_1 = inp_1[:len(inp_1)-1]

        for (i, j) in enumerate(inp_1):
            inp_1[i] = j.split(" follows ")
           
            if inp_1[i][0] not in adict:
                adict[inp_1[i][0]] = inp_1[i][1].split(',')
            else:
                adict[inp_1[i][0]].extend(inp_1[i][1].split(','))
        return adict
    return adict




    
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
