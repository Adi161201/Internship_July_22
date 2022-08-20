import numpy
n,m=map(int,raw_input().split())
n=int(n)
m=int(m)
arr=[]
for i in range(n):
    arr.append(map(int,raw_input().split()))
arr=numpy.array(arr,dtype=int)
sum=numpy.sum(arr,axis=0)
print(numpy.prod(sum))