n=int(raw_input())
a=set(map( int, raw_input().split() ))

m= int(raw_input())
b=set(map( int, raw_input().split() ))

l1=len(a)
l2=len(b)

print( len( (a|b)  ))