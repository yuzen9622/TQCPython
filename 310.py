n=int(input())
sum=0
for i in range(1,n):
    sum+=1/(((i+1)**0.5)+(i**0.5))
print('%.4f'%sum)