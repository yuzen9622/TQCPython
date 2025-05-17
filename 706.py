
c=int(input())

for i in range(c):
  
    sen=input()
    s=set(sen.lower())
    
    if ' ' in s:
        s.remove(' ')
    if len(s)>=26:
        print("True")
    else:
        print("False")
    