n=int(input())

for i in range(1,n+1):
    sum=0
    a=int(input())
    b=a
    while a:
        sum+=a%10
        a//=10
    print("Sum of all digits of {} is {}".format(b,sum))

    