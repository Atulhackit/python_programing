user_input=input('enter a number to find out the sum :')
user_input=int(user_input)
sum=0
i=1

while i<=user_input:
    sum = sum + i
    i+=1
print(sum)