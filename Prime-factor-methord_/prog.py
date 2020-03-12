import math
import datetime

primes = []
expos = []

def loadPrime():
	e_file = open("primeList.txt","r")
	for line in e_file.readlines():
		linedata = line.split()
		for num in linedata :
			if(num != '\n' and num!= 'end.'):
				primes.append(int(num))


loadPrime()

input_num = int(input('Enter a number:'))

def expo_num(input_num, prime_single):
	c = 0;
	while(input_num != 0):
		input_num = input_num/prime_single
		c = c + math.floor(input_num)

	return c
					

e_file = open("out.txt","w")
def call(input_num):
	output = 1
	for prime in primes:
		if(prime>input_num):
			print("END")
			break
		c = expo_num(input_num,prime)	
		output = output* prime ** c
		print("{}^{} * \n".format(prime,c))
		e_file.write("{}^{} + \n".format(prime,c))

	print("0\n")
	e_file.write("Factorial : "+str(output))
	return output	

t1=datetime.datetime.now()
c = call(input_num)
t2=datetime.datetime.now()
d = math.factorial(input_num)
t3=datetime.datetime.now()
print(c)
print("Truth value : "+str(d==c))
print("Time mine : "+str(t2-t1))
print("Time python : "+str(t3-t2))