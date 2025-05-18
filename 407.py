while True:
    y=int(input())
    if y==-9999:
        break
    if y%4==0 and (y%100!=0 or y%400==0):
        print("%d is a leap year."%y)
    else:
        print("%d is not a leap year."%y)