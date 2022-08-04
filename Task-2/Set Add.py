n=int(raw_input())
a=set()
for i in range(n):
    a.add(raw_input())
count=0
for x in a:
    count+=1
    
print(count)