t1=()
t2=()
print("Create tuple1:")
while True:
    n=eval(input())
    if n ==-9999:
        break
    t1+=(n,)
    
print("Create tuple2:")
while True:
    n=eval(input())
    if n ==-9999:
        break
    t2+=(n,)
t1+=t2

l=list(t1)
l.sort()
print(f"Combined tuple before sorting:{t1}")
print(f"Combined list after sorting:{l}")