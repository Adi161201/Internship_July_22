m=int(input())
a= set(map( int , raw_input().split()))
n=int(input())
b=set(map(int, raw_input().split()))

ans = (a|b) -(a & b)
for i in sorted(ans) :
    print(i)
