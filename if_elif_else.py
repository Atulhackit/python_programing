age=input('enter your age :')
age=int(age)
if age<=0:
    print('enter a valid number.')
elif 0<age<=5:
    print('ticket price is 0 .')
elif 5<age<=14:
    print('ticket price is 100.')
elif 14<age<=45:
    print('ticket price is 200.')
else:
    print('ticket price is 250.')