k=int(input())
answer=0
	
while k>=0:
	if k % 5==0:
		answer+=(k//5)
		print(answer)
		break
	k-=3
	answer+=1
else:
	print(-1)
