list=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
numbers=[]
max=list[0][1]
temp=-99999
for x in list: 
    
    if x[1]>max:
        temp_second_last=max
        max=x[1]

names=[]
for i in list: 
    if i[1]==temp_second_last:
        names.append(i[0])

names.sort()
print(names)


scores=[-50,-50,-50,51]
# scores.sort()
# print(scores)
b=set(scores)
print(b)

print(b[-2])


n=2

for i in range(n):
    string=[]
    string = str( input().split(' '))
    print(string)