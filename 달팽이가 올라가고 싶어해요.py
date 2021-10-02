
a,b,v=map(int, input().split())
tide=(v-a)%(a-b)
time=(v-a)//(a-b)
day=0
if tide==0:
	day=time+1
	print(day)
elif tide!=0:
	day=time+2
	print(day)
