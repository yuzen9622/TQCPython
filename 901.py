file=open('./write.txt','w')

for i in range(5):
    file.write(input()+'\n')
file.close()