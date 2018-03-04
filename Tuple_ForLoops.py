tuple1 = (1.5,5,True,"yes")
print(tuple1)
print(tuple1[1])
print(tuple1[0])
print(tuple1[:2])
print(tuple1[1:])
print(tuple1[1:2])

tupleFor = ("bohr","leibniz","einstein")
listNo = []
listNum = [9,8,7,6,5,4,3,2,1,0]

for indexes in tupleFor:
    print(indexes)

for items in listNum[2:8]:
    listNo.append(items)

print(listNo)