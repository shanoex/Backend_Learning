addtwo = lambda num : num + 2
print(addtwo(5))

def funcbuilder(num):
    return lambda x: x + num
addthree = funcbuilder(3)
addten = funcbuilder(10)
print(addthree(5))
print(addten(5))

##############################

numbers=[1,2,3,4,5]
squared = map(lambda x: x*x, numbers)
print(list(squared))

###############################

odd = filter(lambda x: x%2 !=0, numbers)
print(list(odd))