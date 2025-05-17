c=str(input())

if (c.isdigit()):
    print(f'{c} is a number')
elif (c.isalpha()):
    print(f'{c} is an alphabet.')
else:
    print(f'{c} is a symbol.')
    
