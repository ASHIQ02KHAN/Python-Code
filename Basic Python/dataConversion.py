integer = 2025
name = 'Khan'   #string
isHappy = '22'  #string

# print(name + integer)    will show error because string and int can't be combined without conversion 

print(name + str(integer)) 
print(integer + int(isHappy)) 