n=int(input())

for i in range(n,0,-1):
   print(' '*(i-1)+ '*'*(1+2*(n-i)))