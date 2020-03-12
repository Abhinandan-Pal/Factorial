import matplotlib.pyplot as plt
total=int(input("Enter : "))

avg = 0

def fact_1(set_a):
	xy = set_a-1
	x = set_a-1
	y = 1	arr = []
	while(x>=y):
		val =  xy% set_a
		#print(val)
		if val not in arr:
			arr.append(val)
	
		xy = xy + x -y -1
		x= x-1
		y = y+1
	return 	(set_a/2)/len(arr)

#print("CHECK")
#c = 1
#d = 3
#while(c<set_a):
#
#	print(set_a-c)
#	c = c + d
#	d = d+2
num = []
save = []
avg_point = []
for i in range(2,total):
	a = fact_1(i)
	num.append(i)
	save.append(a)
	print(str(i)+ " : "+ str(a))
	avg = avg + a
	avg_point.append(avg/i)

print("\n\nFINAl : "+ str(avg/total))
#print("Len  :"+ str(set_a/2))
#print("Len unique :"+ str(len(arr)))
plt.scatter(num,avg_point)
plt.savefig("trend.pdf")
plt.savefig("trend.png")
plt.show()