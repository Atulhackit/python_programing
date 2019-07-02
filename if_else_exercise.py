user_name=input("enter your name :")
user_age=input('enter your age :')
user_age=int(user_age)
#first_word=user_name[0].lower() 

if user_age>=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print('you can watch coco movie .')
else:
    print('you can not watch coco movie.')