d=dict()
while True:
    k=input("Key: ")
    if k=='end':
        break
    d[k]=input("Value: ")

for i in sorted(d.keys()):
    print(f'{i}: {d[i]}')