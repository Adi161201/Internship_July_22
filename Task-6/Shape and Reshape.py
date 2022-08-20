import numpy
list=[]
temp =raw_input().split(' ')

for i in range(0,9):
    list.append(int(temp[i]))
arr= numpy.array(list).reshape(3,3)
print(arr)