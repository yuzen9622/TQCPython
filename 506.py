def compute(a,b,c):
    tmp=b**2-4*a*c
    if tmp<0:
        print("Your equation has no root.")
    elif tmp==0:
        ans=-b/2*a
        print(ans)
    elif tmp>0:
        print("%.1f, %.1f"%(((-b+tmp**0.5)/(2*a)),((-b-tmp**0.5)/(2*a))))
compute(int(input()),int(input()),int(input()))