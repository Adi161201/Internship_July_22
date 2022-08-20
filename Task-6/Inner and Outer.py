import numpy
arr1=numpy.array( map(int, raw_input().split()), int)
arr2=numpy.array( map(int, raw_input().split()), int)

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))