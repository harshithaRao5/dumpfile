# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recurPower(base, exp):
    if exp == 0:
        return base
    else:
        return base*recurPower(base, exp-1)
def main():
    data = input()
    data = data.split()
    print(recurPower(float(data[0]),int(data[1])))   

if __name__== "__main__":
    main()