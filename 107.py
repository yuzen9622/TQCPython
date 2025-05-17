sum=0
l=[0]*5
for i in range(5):
    l[i]=eval(input())
    sum+=l[i]

print(l[0],l[1],l[2],l[3],l[4])
print("Sum = %.1f"%sum)
print("Average = %.1f"%(sum/5))

