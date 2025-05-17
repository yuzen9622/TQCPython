def compute(x,y):
    while y:
        tmp=y
        y=x%y
        x=tmp
    print(x)
x,y=eval(input())
compute(x,y)
