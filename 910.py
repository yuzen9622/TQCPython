m=fm=0
print("學號 姓名 性別 科系")
with open("read.dat",'r',encoding='utf-8') as f:
    for i in f:
        print(i)
        sp=i.split()
        if sp[2]=='1':
            m+=1
        else:
            fm+=1
print("Number of males:%d"%m)
print("Number of females: %d"%fm)