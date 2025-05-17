f=open("./data.txt",'a+')
for i in range(5):
    f.write(input()+'\n')
  
f.seek(0)
print("Append completed!")
print('Content of "data.txt":')
print(f.read())
    
