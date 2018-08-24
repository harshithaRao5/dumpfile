#define the gen_primes function here
def genPrimes():
	while True:
        if is_prime(number):
            yield number
        	print(number)
    

def main():
	datainput()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.next()
	    if i%b == 0:
	        print p
	
if __name__== "__main__":
	main()
