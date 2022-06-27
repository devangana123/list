number=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=[]
b=[]
while i<len(number):
    if number[i]%2==0:
        a.append(number[i])
    else:
        b.append(number[i])
    i=i+1
print("even number",a)
print("odd number",b)

