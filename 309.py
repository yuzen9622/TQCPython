n=int(input())
b=float(input())
m=int(input())

print("Month \t  Amount")
for i in range(1,m+1):
    n+=n*b/1200
    print("%3d \t %.2f"%(i,n))
 