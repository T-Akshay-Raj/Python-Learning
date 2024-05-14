# Define a basic function
def basicFunction():
    print("Hello")


# Function that takes two arguments
def twoArgumentFunction(arg1, arg2):
    print(arg1, " ", arg2)


# Function with return values
def returnSquare(arg1):
    return arg1 * arg1


# Function with default value for an argument
def power(arg1, n=1):
    result = 1
    for i in range(n):
        result = result * arg1
    return result\
    
# Function with variable number of arguments
def multi_add(*args):
    result=0
    for arg in args:
     result=result+arg
    return result

# Function to return more than one value
def multi_return(*args):
    sum = 0
    product=1
    for arg in args:
        sum=sum+arg
        product=product*arg
    return sum,product


if __name__ == '__main__':
    basicFunction()  # or print(basicFunction())
    twoArgumentFunction("abc", 10)  # abc 10

    print(returnSquare(2))  # or returnSquare(2)  # 4
    print(power(2, ))  # not passing any power, so takes default as 1
    print(power(2, 3))  # 8

    # python allows calling with different order of arguments, provided each argument is associated with its appropriate name
    print(power(n=3, arg1=2))  # 8

    # Variable number of argument in a function
    print(multi_add(10,20,30))
    print(multi_add(1,2,3,4,5,6,7,8,9,10))

    print(multi_return(1,2,3,4,5,6,7,8,9,10)) # 55, 3628800

# multi values returned can be saved to tuple to access later
    myTuple=multi_return(1,2,3,4,5,6,7,8,9,10)
    print("Sum = ",myTuple[0]) # 55
    print("Product =",myTuple[1]) # 3628800

# output:
# Hello
# abc   10
# 4
# 2
# 8
# 8
