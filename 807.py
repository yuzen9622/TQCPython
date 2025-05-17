s=input().split(" ")
sum=0
for c in s:
    sum+=int(c)
print(f'Total = {sum}')
print(f'Average = {sum/len(s)}')