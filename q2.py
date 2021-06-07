st=input()
c=0
t=len(st)
for i in range(t):
    if st[i]=='1':
        c+=1
st=''
for i in range(0,c):
    st+='1'
for i in range(c,t):
    st+='0'
print(st)
