# l=input("enter the letters:-")
# for i in range(len(l)):
#     if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u":
#         print(l[i],"vowel")
#     else:
#         print(l[i],"consonents")



l=input("enter the letters:-")
i=0
while i<len(l):
    if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u":
        print(l[i],":-vowel")
    else:
        print(l[i],":-consonents")
    i+=1