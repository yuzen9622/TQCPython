
with open(input(),"r+") as file:
    s1=input()
    s2=input()
    print("=== Before the replacement")
    data=file.read()
    print(data)
    data=data.replace(s1,s2)
    print("=== After the replacement")
    print(data)
    file.seek(0)
    file.write(data)