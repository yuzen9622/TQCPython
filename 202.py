n=int(input())

if n%3==0 and n%5!=0:
    print(f'{n} is a multiple of 3.')
elif n%5==0 and n%3!=0:
    print(f'{n} is a multiple of 5.')
elif n%5==0 and n%3==0:
    print(f'{n} is a multiple of 3 and 5.')
else:
    print(f'{n} is not a multiple of 3 or 5.')