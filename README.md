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


## Basic

### datatypes:
- int: myInt=5
- float: myfloat=6.5
- String: myString="String example"
- boolean: mybool=True
- List: myList=[0,1,"two",3.3,False]
- Tuple: myTuple=(0,1,2)
- Dictionary: myDict={"one":1, "two":2}


- del statement: to delete any variable

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


## File Management
### Read and write using built in python file methods
1. Open file for writing or create if not exists
e.g. 
f=open("textfile.txt", "w+")
f.write("some text")
2. Append Mode
e.g. open("textfile.txt","a+")
f.write("some text")
3. Read file
e.g. open("textfile.txt", "r")
content=f.readlines() or f.read()


### Using OS path Utils
### Using Shell Utils


## Using Dates and Times
- DateTime
- Formatting DateTime
- TimeDelta
- Calendar

## Internet Data
- InetData
- Working with JSON
- Parsing HTML
- Parsing XML

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
Answer: Ogres are ften flh
- What is the proper code for creating a "for" loop that will execute 9 times starting at the number 6?
	- for i in range(6, 16):

- Of the following options, which is logically equivalent to the code below? maxnum = x if (x>y) else yt
```
maxnum = y
	  if (x>y):
    	    maxnum = x
```
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
 print(a)
```
Answer:	- 4

- What is the proper syntax for accessing the fourth element of the following sequence? values = [1,3,5,7,9,11,13]
	- values[3]

- Class Fruit is derived from the class Food. Which is the correct way for Fruit to call a function of its parent class?
	- super().SetPrice(50)

- Why is this code below often added to a Python program file?

```
if __name__ == "__main__":
    main()
```
Answer: It executes the main() function only if this file is executed as the main program.

- Given this variable, how can you print it reversed? s="123456"
	- print(s[::-1])

- What will be the result of the following code?

```
thestr = "This is a string"
print(thestr)
thestr = 5 
```
Answer: The code will print "This is a string" and set the value of thestr to 5.

- What will this code print?

```
try:
    x=int("five")
except ValueError:
    print("There is a value error.")
finally:
    print("Something went wrong.")
```
Answer: There is a value error. Something went wrong.

- Which of these is not one of the main Python data types?
	- matrix
- What is a Python library module?
	- pre-built code you can use in your program
- What is the correct way to define a class named "Point" that is initialized with x and y coordinate values?
``` 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
```
- How many numbers will be printed with this code?

```
x=0
while(x<5):
    print(x)
    x=x-1
```
Answer: an infinite number

- When creating a match-case block, which line defines the default case?
	- case _:

- What will this print, assuming runtest() is a function that does not return a value? print(runtest())
	- the value None

- What will this code print?
```
var="123456789"
print(var[1:6:2])
```
Answer: 246

- What is the purpose of the finally section of an exception handling statement?
	- The code in the finally section always runs, so it's a good place to clean up any allocated resources.

- Of the following, which is the most correct code for the "except" section to accompany the following "try" section to handle a divide by zero exception?

```
# assume two integer variables, x and y
try:
    result = x / y
```
Answer:
```
		except ZeroDivisionError as e:
    print("A divide by zero error occurred", e)
```

- What is the correct way to import Python's math module and then use the square root function?
	- import math x = math.sqrt(16)

- What is the purpose of the super() function when working with Python classes?
	- to access methods and properties within the parent class of the class where super() is being called from

- What does the os.listdir() function return?
	- files and subdirectories in the current directory
- What is the correct code to rename a given file from "file.txt" to "data.dat" assuming that the os module has been imported?
	- os.rename("file.txt", "data.dat")

- While _____ checks whether a path exists, _____ checks whether a path is a file.
	- path.exists(); path.isfile()

- What mistake, if any, is present in this code? shutil.make_archive("myfile","myfolder")
	- The archive format is not specified.

- What is the correct code to use to open a file named "thefile.txt" for appending data and to create the file if it doesn't exist?
	- f = open("thefile.txt", "a+")

- Which code reads the entire contents of a file line by line into an array?
	- contents=myfile.readlines()

- What will be printed, assuming you are on a Windows machine and the working directory is set to C:\Projects? print(path.realpath("myfile.txt"))
	- C:\Projects\myfile.txt

- Of the following examples, which one will correctly print the name of tomorrow's day of the week?
```
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])
```

- What is another way to implement this code? x = datetime.date(datetime.now())
	- x = date.today()

- What are all the argument(s), if any, expected by the calendar.monthcalendar() function?
	- a year and a month, as integers

- What calendar class will you use to create a Python list of weeks for a given month, where each week is a Python list of days?
	- monthcalendar()

- Your program needs to alert the user if their password expires in less than 7 days. Assuming the password expiration date is in the texp variable, what option will work best?
	- if ((texp-date.today()).days<7):
    	- print("password will expire soon!")

- Which strftime() code prints the abbreviated weekday name?
	- %a
- Of the following examples, which one will generate a date and time output in the following format? 13-Mar-2020 16:42:58
```
from datetime import datetime
 now=datetime.now()
 print(now.strftime("%d-%b-%Y %H:%M:%S"))
```

- Which code can you use to print a text-formatted monthly calendar for every month in the current year, using Sunday as the first day of the week?
```
import calendar
import datetime
year = datetime.datetime.now().year
cal = calendar.TextCalendar(calendar.SUNDAY)
for m in range(1,13):
    print(cal.formatmonth(year, m, 0, 0))
```
- You need to calculate tomorrow's date. Which option should you choose?

```
 today = date.today()

 # Option A:
 tomorrow = today+timedelta(days=1)
 # Option B:
 tomorrow = date(today.year,today.month,today.day+1)
```
Answer: Option A

- Given the XML below, what would be the correct Python code to add a third item to the list that has a yellow color and a small size?

```
 <?xml version="1.0" encoding="UTF-8" ?>
  <catalog>
  <item color="blue" size="large"/>
  <item color="red" size="medium"/>
  </catalog>
```
Answer:
```
doc = xml.dom.minidom.parse("my.xml")
newItem = doc.createElement("item")
newItem.setAttribute("color", "yellow")
newItem.setAttribute("size", "small")
doc.firstChild.appendChild(newItem)
```

- What is the name of the base class that Python provides that you must derive a class from to work with HTML?
	- HTMLParser

- Given the following JSON data stored in a variable named "theJSON", how can you list only the skill names?

```
 {
  "name": "John",
  "title": "Python Developer",
  "skills": [{
  "name": "coding",
  "level": "expert"
  },
  {
  "name": "documentation",
  "level": "basic"
  }]
  }
```
```
for i in theJSON["skills"]:
  print(i["name"])
```

- What is returned by the getpos() method of the HTML parsing parent class?
	- the line and position where the specific element starts

- Given the JSON data below is loaded to the variable x, which call will print "jane"?
```

{
"users": [
    {"name":"john","gender":"male"},
    {"name":"jane","gender":"female"},
    {"name":"jim","gender":"male"},
    {"name":"jackie","gender":"female"}
]
}
```
	- print(x["users"][1]["name"])

- How do you send an HTTP request?
	- urllib.request.urlopen("https://mysite.com")

- The following code, which is intended to write the HTML source content of the google.com homepage to the console, is missing a line at the ??? placeholder. What should this line be?

```
import urllib.request
webUrl = urllib.request.urlopen("http://www.google.com")
???
print(results)
```
	- Answer: results = webUrl.read()

- What value should be returned by the call to the URL request getcode() method to confirm that the specified URL has successfully returned data?
	- 200
