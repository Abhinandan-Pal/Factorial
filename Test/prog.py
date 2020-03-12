import math
To_be_checked = int(input("Enter the number to be verified : "))


xy = (To_be_checked-1)/2
x = (To_be_checked-1)/2
y = 1
array_seriese = []
	


for i in range (math.floor((To_be_checked-1)/4)):
	while(x>y):
		val =  xy% To_be_checked
		#print(val)
		array_seriese.append(xy)
		xy = xy + x -y -1
		x= x-1
		y = y+1
if((To_be_checked-1)%4 != 0):
	array_seriese.append(math.ceil(To_be_checked/4))
print(array_seriese)