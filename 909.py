f=open("data.dat","w+")

for i in range(5):
    f.write(input()+'\n')
print("The content of \"data.dat\":")
f.seek(0)
for i in f:
    print(i)
# with open("data.dat","w",encoding="UTF-8") as fp:
#   for i in range(5):
#       fp.write(input()+"\n")
 
# print('The content of "data.dat":')
# with open("data.dat","r",encoding="UTF-8") as fp:
#   for i in fp:
#       print(i)