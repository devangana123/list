number=[50,40,23,70,53,12,5,10,7]
i=0
max=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    i=i+1
print("greater number is",max)
i=0
max1=0
while i<len(number):
    if number[i]>max1:
        if number[i]!=max:
            max1=number[i]
    i=i+1
print("second greater number is",max1)  
i=0
max2=0
while i<len(number):
    if number[i]>max2:
        if number[i]!=max1 and number[i]!=max:
            max2=number[i]
    i=i+1
print("third greater number is",max2)
