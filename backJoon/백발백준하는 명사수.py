x, y,r = map(int, input().split()) 
xx,yy,rr=map(int, input().split())
if ((x-xx)*(x-xx)+(y-yy)*(y-yy)>=(r+rr)*(r+rr)):
		print('NO')
else:
		print('YES')
