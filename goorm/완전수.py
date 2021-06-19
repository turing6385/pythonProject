def sos(r):
	answer = 0 
	for i in range(1,r): 
		if r%i==0: 
			answer += i 
	
	if r==answer:
		return True
	else:
		return False

	

a, b = input().split()
a=int(a)
b=int(b)
for i in range(a,b+1):
	if sos(i)==True:
		print(i,end=' ')
	else:
		continue
	
