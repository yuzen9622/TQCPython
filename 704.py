s=set()
while True:
    n=int(input())
    if n==-9999:
        break
    s.add(n)
print(f'Length: {len(s)}')
print(f'Max: {max(s)}')
print(f'Min: {min(s)}')
print(f'Sum: {sum(s)}')