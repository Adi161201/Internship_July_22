import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    list=[]
    ans= numpy.array(arr,float)
    for i in range(ans.size-1,-1,-1):
        list.append(ans[i])
    
    return numpy.array(list)
        
    

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)