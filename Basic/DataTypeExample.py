# Basic datatype in Python are Number, String, Boolean, Sequence, Dictionaries
# int:
myInt = 5
# float:
myfloat = 6.5
# String:
myString = "String example"
# boolean:
mybool = True
# List:
myList = [0, 1, "two", 3.3, False]
# Tuple:
myTuple = (0, 1, 2)
# Dictionary:
myDict = {"one": 1, "two": 2}

print(myInt)
print(myfloat)
print(myString)
print(mybool)
print(myList)
print(myTuple)
print(myDict)

# Re-Declaring Variable
myInt = "abc"
print(myInt)  # abc

# Accessing individual elements from sequence types using [], zero based index
print(myList[1])  # 1
print(myTuple[2])  # 2

# Use Slice to get part of sequence
print(myList[2:5])  # "two", 3.3, False]

# Use Slice get parts with step
print(myList[1:5:2])  # [1, 3.3]

# Use Slice to reverse
print(myList[::-1])  # [False, 3.3, 'two', 1, 0]

# Accessing Dictionary using keys
print(myDict["one"])  # 1

# ERROR: variable of different type cannot be combined
#print(myString+123) # TypeError: can only concatenate str (not "int") to str

# Fix to above error is 
print(myString+str(123))
