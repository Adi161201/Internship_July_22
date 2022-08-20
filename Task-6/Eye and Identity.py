import numpy
numpy.set_printoptions(legacy='1.13')

shape=map(int, raw_input().split())

print(numpy.eye(shape[0],shape[1], k=0))