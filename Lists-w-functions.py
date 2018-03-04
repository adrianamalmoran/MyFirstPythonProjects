integers = [0,1,2,3,4,5]
strings = ["one","two","three","four"]
floats = [1.1,2.2,3.3,4.4,5.5]

def passed(list):
    return list

print(passed(integers))
print(passed(strings))
print(passed(floats))

def index(list):
    return list[3]

print(index(integers))
print(index(strings))
print(index(floats))

def products(list):
    total = 0
    for integers in list:
        total = total * integers
    return total

print(products(integers))

def concat(list):
    str = ""
    for count in list:
        str = str + count + " "
    return str

print(concat(strings))

def quoti(list):
    quotient = 10.0
    for floats in list:
        quotient = quotient / floats
    return quotient

print(quoti(floats))

def manip(list):
    list.append(6)
    list.remove(2)
    list.insert(4,18)
    return list

print(manip(integers))