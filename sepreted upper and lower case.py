a=[1,2,"a1",3,"b2","11"]
i=0
b=[]
while i<len(a):
    if type(a[i])==str:
       b.append(a[i])
    i=i+1
print(b)


# a=[[1,2],[3,4],[5],[8,9]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b. append(a[i][j])
#             j=j+1
#     i=i+1
# print(b)