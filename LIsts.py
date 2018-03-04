listString = ["one","two","three","four"]
listNum = [1,2,3]
list3 = ["one",2,True,5.4,"list"]

print(listString)
print(listNum[1])
print(list3[2])

list1 = [1,2,3]
list1[0]=2
list1[1]=3
list1[2]=4
list1.append(6)

print(list1)

listVar = [0,1,2,3,4,5,6]
print(listVar[0:4])
print(listVar[2:5])
print(listVar[1:6])

listBob = ["Bob Dylan","Like a","Rolling Stone"]
print(listBob.index("Rolling Stone"))
listBob.insert(0,1965)
print(listBob)

list = ["McCartney","Lennon","Starr","Harrison","Sutcliffe"]
list.remove("Sutcliffe")
print(list)
print(list.pop(1))
print(list.pop(2))
print(list)
