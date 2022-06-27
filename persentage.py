p=[1,2,3,4,5,6,7,8,9]
i=0
a=[]
b=[]
sum1=0
sum2=0
count=0
count1=0
while i<len(p):
    if p[i]%2==0:
        a.append(p[i])
        sum1=sum1+p[i]
        count=count+1
        z=sum1/count*100
    else:
        b.append(p[i])
        sum2=sum2+p[i]
        count1=count1+1
        x=sum2/count1*100
    i=i+1
print("even number",a,"sum=",sum1,"count=",count,"persentage",z)
print("odd number",b,"sum=",sum2,"count=",count1,"persentage",x)
