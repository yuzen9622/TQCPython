f=open("./tqc-python/read.txt","r") 

width=[]
height=[]
w=f.readlines()
tall=0
heav=0
tname=""
hname=""
for i in w:
    print(i)
    sp=i.split()
    width.append(eval(sp[2]))
    height.append(eval(sp[1]))    
    if eval(sp[1])>tall:
        tall=eval(sp[1])
        tname=sp[0]
    if eval(sp[2])>heav:
        heav=eval(sp[2])
        hname=sp[0]
print(f'Average height: {sum(height)/len(w):.2f}')
print(f'Average weight: {sum(width)/len(w):.2f}')
print(f'The tallest is {tname} with {tall:.2f}cm')
print(f'The heaviest is {hname} with {heav:.2f}cm')

