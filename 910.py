m=fm=0
f=open("read.dat",'r',encoding='utf-8')
w=f.readlines()
for i in w:
    print(i)
    sp=i.split()
    if sp[2]=='1':
        m+=1
    elif sp[2]=='0':
        fm+=1
print("Number of males: %d"%m)
print("Number of females: %d"%fm)