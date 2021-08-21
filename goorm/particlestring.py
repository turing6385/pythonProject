num_list = input()
o = []					
n= len(num_list)								
k= int(input())	 
for i in range(0,n):
	for j in range(n-i):
		if num_list[j:j+i+1] not in o:
			o.append(num_list[j:j+i+1])
o.sort()			
print(o[k-1])
