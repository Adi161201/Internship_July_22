n=int(raw_input())
a=set(raw_input().split())

m=int(raw_input())
b=set(raw_input().split())

print(len( (a|b)- (a & b)))