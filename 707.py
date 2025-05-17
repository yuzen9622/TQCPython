s1=set()
s2=set()

print("Enter group X's subjects:")

while True:
    s=input()
    if s=='end':
        break
    s1.add(s)
print("Enter group Y's subjects:")

while True:
    s=input()
    if s=='end':
        break
    s2.add(s)

print(sorted(s1.union(s2)))
print(sorted(s1.intersection(s2)))
print(sorted(s2.difference(s1)))
print(sorted(s2.symmetric_difference(s1)))