with open(f'./tqc-python/{input()}','r')as f:
    n=eval(input())
    w=f.read()
    sp=w.split()
    s=sorted(set(sp))
    for i in s:   
        if sp.count(i)==n:
            print(i)