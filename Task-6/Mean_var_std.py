import numpy
n,m=map(int,raw_input().split())
n=int(n)
m=int(m)
arr=[]
for i in range(n):
    arr.append(map(int,raw_input().split()))
arr=numpy.array(arr,dtype=int)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.round( numpy.std(arr,axis=None) ,11))