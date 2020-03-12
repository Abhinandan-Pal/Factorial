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
		array_seriese.append(val)
		xy = xy + x -y -1
		x= x-1
		y = y+1
if((To_be_checked-1)%4 != 0):
	array_seriese.append(math.ceil(To_be_checked/4))
#print(array_seriese)

def minimize(curr_arr):
	new_arr = []
	
	for i in range(math.floor(len(curr_arr)/2)):
		val = (curr_arr[i]*curr_arr[-i-1])%To_be_checked
		new_arr.append(val)
	if((len(curr_arr)%2)!=0):
		new_arr.append(curr_arr[math.floor(len(curr_arr)/2)])
	#print(new_arr)
	if(len(new_arr)==1):
		return new_arr[0]		
	return minimize(new_arr)	

minimized_val =  minimize(array_seriese)
minimized_val = minimized_val**2 *(1 if ((To_be_checked-1)%4== 0)else-1)
print (minimized_val%To_be_checked == (To_be_checked-1))		