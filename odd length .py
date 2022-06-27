list=[2,7,2,8,3,7,9,5,8,3,4]
l=[]
odd=1
i=0
while i<=len(list):
    if odd%2!=0:
        l.append(list[i])
    odd+=1
    i+=1
print(l)