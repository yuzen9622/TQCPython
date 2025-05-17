t=()
while True:
    s=input()
    if s=='end':
        break
    t+=(s,)
print(t)
print(t[0:3])
print(t[-3:])