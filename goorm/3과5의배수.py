a= int(input())
p=0
s=0
t=0
y=0
for i in range(1, a+1):
	t=3*i
	if t <= a:
		s+=3*i
	else :
			break

for o in range(1,a+1):
	y=5*o
	if y <= a :
		s+=5*o
	else :
		break

for u in range(1,a+1):
	if 15*u<=a:
		s-=15*u	
	else :
			break
print(s)	
		
