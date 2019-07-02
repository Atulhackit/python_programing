name, age =input("enter your name and age :").split()

print(name + ' you are '+str(age)+' years old')#normal form
print('{} you are {} years old'.format(name, age))#method1
print(f"{name} you are {age} year old")
