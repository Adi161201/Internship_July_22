if __name__ == '__main__':
    N = int(input())
    arr=[]
   
    for i in range(0,N):
        
        string1 =input().split()
        if string1[0]=='insert':
            arr.insert(int(string1[1]),int(string1[2]))
        elif string1[0]=='print':
            print(arr)
        elif string1[0]=='remove':
            if int(string1[1]) in arr :
                arr.remove(int(string1[1]))
            
        elif string1[0]=='append':
            arr.append(int(string1[1]))
            
        elif string1[0]=='sort':
            arr.sort()
        elif string1[0]=='pop':
            arr.pop()
        elif string1[0]=='reverse':
            arr.reverse()