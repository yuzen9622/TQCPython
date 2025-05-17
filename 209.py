x1=int(input())
y1=int(input())

pos=((x1-5)**2 + (y1-6)**2)**0.5

if pos<=15:
    print("Inside")
else:
    print("Outside")