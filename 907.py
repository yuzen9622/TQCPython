
l=w=c=0

with open(f'./tqc-python/{input()}','r+') as f:
    lines=f.readlines()
    for line in lines:
        l+=1
        w+=len(line.split())
        c+=sum([len(c) for c in line.split()])
print("%d line(s)"%l)
print("%d word(s)"%w)
print("%d character(s)"%c)