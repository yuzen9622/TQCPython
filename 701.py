l=[]

while True:
    n=eval(input())
    if n ==-9999:
        break
    l.append(n)
t=tuple(l)
print(t)
print(f'Length: {len(t)}')
print(f'Max: {max(t)}')
print(f'Min: {min(t)}')
print(f'Sum: {sum(t)}')

    