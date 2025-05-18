d=dict()
while True:
    k=input('Key: ')
    if k=="end":
        break
    d[k]=input('Value: ')
q=input("Search key: ")
print("True") if d.get(q) else print("False")