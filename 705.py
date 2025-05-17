s1=set()
s2=set()
s3=set()
print("Input to set1:")
for  i in range(5):
    n=int(input())
    s1.add(n)
print("Input to set2:")   
for  i in range(3):
    n=int(input())
    s2.add(n)
print("Input to set3:")
for  i in range(9):
    n=int(input())
    s3.add(n)

print(f'set2 is subset of set1:{s2.issubset(s1)}')
print(f'set3 is superset of set1:{s3.issuperset(s1)}')