# Python-Learning

## Learning python

### Python Shell:
cmd:
python

e.g. 
1. 2+2
2. print("Hello World")
3. name=input("Enter name")
   enter name and 
   print(name) or name



datatypes:
int: myInt=5
float: myfloat=6.5
String: myString="String example"
boolean: mybool=True
List: myList=[0,1,"two",3.3,False]
Tuple: myTuple=(0,1,2)
Dictionary: myDict={"one":1, "two":2}


del statement: to delete any variable

### Functions
- Basic function
- One or More than one argument function
- Variable number of Argument function
- Function with return type
- Function with more than one return values
### Conditional Statements
- if
- if else
- if elif else
- match-case from python 3.10
### Loops
- While loop
- For loop
- Use break and continue statements
- Using enumerate function to get index
### Classes
- classes, base class and child class(Inheritance)
### Exception handling
- using try and except




### Recap
- What is the output of the code below?

```
thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)
```
	- Ogres are ften flh
- What is the proper code for creating a "for" loop that will execute 9 times starting at the number 6?
	- for i in range(6, 16):

- Of the following options, which is logically equivalent to the code below? maxnum = x if (x>y) else yt
	- ```maxnum = y
	  if (x>y):
    	    maxnum = x```
- What will this line do? value=input("2+2=")
	- It will store the user's input into a variable.

- What is the right way to define a function that takes one named argument followed by a variable number of arguments?
	- def func(arg1, *args)
- What will the following code print?

```
def inc(a,b=1):
    return(a+b)

 a=inc(1)
 a=inc(a,a)
 print(a)```
	- 4

- What is the proper syntax for accessing the fourth element of the following sequence? values = [1,3,5,7,9,11,13]
	- values[3]

- Class Fruit is derived from the class Food. Which is the correct way for Fruit to call a function of its parent class?
	- super().SetPrice(50)

- Why is this code below often added to a Python program file?

```
if __name__ == "__main__":
    main()
```
	- It executes the main() function only if this file is executed as the main program.

- Given this variable, how can you print it reversed? s="123456"
	- print(s[::-1])

- What will be the result of the following code?

```
thestr = "This is a string"
print(thestr)
thestr = 5 
```
	- The code will print "This is a string" and set the value of thestr to 5.

- What will this code print?

```
try:
    x=int("five")
except ValueError:
    print("There is a value error.")
finally:
    print("Something went wrong.")
```
	- There is a value error. Something went wrong.

- Which of these is not one of the main Python data types?
	- matrix
- What is a Python library module?
	- pre-built code you can use in your program
- What is the correct way to define a class named "Point" that is initialized with x and y coordinate values?
	-
   ``` class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y ```

- How many numbers will be printed with this code?

```
x=0
while(x<5):
    print(x)
    x=x-1
```
	- an infinite number

- When creating a match-case block, which line defines the default case?
	- case _:

- What will this print, assuming runtest() is a function that does not return a value? print(runtest())
	- the value None

- What will this code print?
```

var="123456789"
print(var[1:6:2])
```
	- 246

- What is the purpose of the finally section of an exception handling statement?
	- The code in the finally section always runs, so it's a good place to clean up any allocated resources.

- Of the following, which is the most correct code for the "except" section to accompany the following "try" section to handle a divide by zero exception?

```
# assume two integer variables, x and y
try:
    result = x / y
```
	- ```
		except ZeroDivisionError as e:
    print("A divide by zero error occurred", e)
	```

- What is the correct way to import Python's math module and then use the square root function?
	- import math x = math.sqrt(16)

- What is the purpose of the super() function when working with Python classes?
	- to access methods and properties within the parent class of the class where super() is being called from
