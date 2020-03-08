last = int(input("Enter a number"))
x = 1;
for i in range(1,last):
	print(str(i)+" : "+ str(x) + " " +str((i)**2 ==x))
	x = x + 2*i + 1

