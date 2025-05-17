n=int(input())
m=int(input())

def compute(r,c):
    for i in range(r):
        for j in range(c):
            x=j-i
            print("%4d"%x,end="")
        print()

compute(n,m)