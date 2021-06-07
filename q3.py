st=input()
n=int(input())

if len(st)>n:
    st=st[0:n]+st[n+1:]
print(st)
