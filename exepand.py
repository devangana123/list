string=input("enter the number")
b=""
i=0
while i<len(string):
    b+=string[i]
    j=1
    while j<=(len(string)-(i+1)):
        b+="0"
        j+=1
    if i == (len(string)-1):
        break                                                 
    else:
        b+="+"
    i+=1
print(b)
