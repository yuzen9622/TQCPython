n=int(input())

if n>=8000 and n<18000:
    print(n*0.95)
elif n>=18000 and n<28000:
    print(n*0.9)
elif n>=28000 and n<38000:
    print(n*0.8)
else:
    print(n*0.7)

