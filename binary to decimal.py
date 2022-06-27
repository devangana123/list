binary=[1,0,1,1]
a=0
c=0
for i in range(-1,-(len(binary)+1),-1):
	b=binary[i]
	if b==1:
		c+=2**a
	a+=1
print("Bianry to Decimal is :- ",c)
