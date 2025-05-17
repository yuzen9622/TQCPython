d1=dict()
d2=dict()
print("Create dict1:")
while True:
    key=input("Key:")
    if key =='end':
        break
    v=input("Value:")
    d1[key]=v
print("Create dict2:")
while True:
    key=input("Key:")
    if key =='end':
        break
    v=input("Value:")
    d2[key]=v
d1.update(d2)
for i in sorted(d1.keys()):
    print(f'{i}:{d1[i]}')