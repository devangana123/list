decimal = int(input("Enter number which you want to convert: "))
num = " "
while decimal != 0:
	num = str(decimal % 2) + num
	decimal //= 2
print(num) 