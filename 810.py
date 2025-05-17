for i in range(eval(input())):
    data=list(map(float,input().split()))
    print(f'{max(data)-min(data):.2f}')