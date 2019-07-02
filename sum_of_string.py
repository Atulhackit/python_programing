user_input=input('enter a number having more then one digit :')
lenght=len(user_input)

sum=0
i=0
while i<lenght:
    sum+=int(user_input[i])
    i+=1
print(sum)