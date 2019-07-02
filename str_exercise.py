name,char =input('enter your name and character ').split(",")

print(f"length of string : {len(name)}")
print(f"character count : {name.lower().strip().count(char.lower().strip())}")
#name.lower().strip().count(char.lower().strip())


