s=input()

sum=0
for c in s:
    print(f"ASCII code for '{c}' is {str(ord(c))}")
    sum+=ord(c)
print(sum)