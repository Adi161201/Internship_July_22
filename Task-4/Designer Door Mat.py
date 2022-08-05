l=(input().split())
n=int(l[0])
m=int(l[1])


a='-'
b=1
c='.|.'
d=3

i=1
b=1
while(i<= n):
    if(i<= (n//2)):
        #upper
        temp = m - d*b
        if( temp>=3):
            print(a*(temp//2),c*b,a*(temp//2))
        b=b+2

    #middle
    if(i== (n//2)+1):
        print(a*((m-7)//2),'WELCOME', a*((m-7)//2) )
        b=b-2
            
        
    #lower
    if(i>(n//2)):
        if(b>=1):
            temp = m - d*b
            if( temp>3):
                print(a*(temp//2),c*b,a*(temp//2))
            b=b-2

       
    i=i+1




    