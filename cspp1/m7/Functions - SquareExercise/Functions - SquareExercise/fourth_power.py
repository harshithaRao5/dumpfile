def square(x_int):
    x_int = x_int**4
    return x_int
def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if(temp[1] == '0'):
        print(square(int(float(str(data)))))
    else:
        print(square(data))
if __name__== "__main__":
    main()
