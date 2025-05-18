f=input()
delete=input()
with open(f,'r+',encoding="utf-8") as file:
    print("=== Before th deletion")
    data=file.read()    
    print(data)
    data=data.replace(delete,"")
    
    print("=== After th deletion")
    print(data)
    file.seek(0)
    file.write(data)
    