name=input('enter your name:')
temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} :  {name.count(name[i])}")
        temp+=name[i]
## name.count(name[i])
# i=0
# temp=""
# while i<len(name):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp+=name[i]
#     i+=1


