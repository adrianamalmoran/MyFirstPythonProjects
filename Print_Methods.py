str1 = 'hello' + ' world'
var1 = 11
var2 = 38
str2 = str(var1)+str(var2)

print(str1)
print(str2)

fave_rest=input('What is your favorite restaraunt?')
fave_place=input('Where would you like to visit?')
nick=input('What is your nickname? If you don\'t have a nickname, what is your first name?')

str3 = 'Your favorite restaraunt is %s, the place you want to visit is %s, and your name is %s'%(fave_rest,fave_place,nick)
print(str3)