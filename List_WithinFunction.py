list1 = [0,1,2,3,4,5,6]

def printList(list):
    for index in list:
        print(index)

printList(list1)

list2=range(0,10)
list3=range(4,7)
list4=range(5,21,5)

def returns(input):
    return (list(input))

print(returns(list2))

def iterates(input):
    for index in range(0,len(input)):
        print(input[index])

iterates(list2)