def sos(string):
    r=0
    for ch in range(len(string)):
        if string[ch]=='(':
            r+=1
        elif string[ch]==')':
            r-=1
        if r==-1:
            break
    if r==0:
        print('YES')
    else :
        print('NO')

a=int(input())
for t in range(a):
    string = str(input())
    sos(string)
