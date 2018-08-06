"""Exercise:square
 given a number returns square using functions"""
def square(x_int):
    """code starts here"""
    x_int = x_int**2
    return x_int
def main():
    '''main function'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))
if __name__ == "__main__":
    main()
