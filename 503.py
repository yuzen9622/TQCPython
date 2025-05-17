def compute(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    print(sum)
compute(int(input()),int(input()))