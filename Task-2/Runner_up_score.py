n = int(input())
arr = []
for i in range(0,n):
    temp=int(input())
    arr.append(temp)

max = arr[0]
smaller=-99999
for i in range(1, len(arr)):
    if arr[i]> max :
        smaller=max 
        max=arr[i]
    elif arr[i]==max: pass
    else:
        if(arr[i] > smaller): smaller=arr[i];
        else : pass
        
print(smaller)