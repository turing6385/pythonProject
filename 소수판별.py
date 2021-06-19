a=int(input())
sos=True
for i in range(2,a):
	if a%i==0:
		sos= False
		break
	else :
		continue
if sos:
	print('True')
else :
	print('False')
		
