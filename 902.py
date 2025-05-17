n=open("./tqc-python/read.txt",'r')

w=n.read()
sp=w.split()
total=0
for i in sp:
    total+=int(i)
print(total)