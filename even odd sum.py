number=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
a=[]
b=[]
while i<len(number):
    sum=sum+number[i]
    if number[i]%2==0:
        a.append(number[i])
    else:
        b.append(number[i])
    i=i+1
print("the sum of the list",sum)
print("even number",a)
print("odd number",b)
i=0
sum1=0
while i<len(a):
    sum1=sum1+a[i]
    i=i+1
print("sum of the even number",sum1)
i=0
sum2=0
while i<len(b):
    sum2=sum2+b[i]
    i=i+1
print("sum of odd number",sum2)
