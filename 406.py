
while True:

    h=int(input())
    w=int(input())
    if h==-9999:
         break

    h/=100
    bmi=0
    bmi=w/h**2
    print("BMI: %.2f"%bmi)
    if bmi<18.5:
        print("State: under weight")
    elif bmi>=18.5 and bmi<25:
         print("State: normal")
    elif bmi>=25 and bmi<30:
          print("State: over weight")
    else:
         print("State: fat")