total1=0
total2=0
total_null=0
for i in range(5):
    a=int(input())
    if a==1:
        total1+=1
    elif a==2:
        total2+=1
    else:
        total_null+=1
    print("Total votes of No.1: Nami = %d"%total1)
    print("Total votes of No.1: Chopper = %d"%total2)
    print("Total null votes = %d"%total_null)
if total1>total2:
    print("=> No.1 Nami won the election.")
elif total2>total1:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")
