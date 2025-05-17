s=input()
b=False
for c in s:
    if c.isupper():
       b=True
if len(s)>=8 and b and s.isalnum():
    print("Valid password") 
else:
    print("Invalid password")