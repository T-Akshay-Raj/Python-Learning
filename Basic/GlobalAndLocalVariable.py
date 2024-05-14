# Global Variable Vs Local Variable
name="global"

def someFuntion():
    name="local" # local variable whose scope is within someFunction()
    print("Name is : ",name)

# Update global variable using keyword global
def updateGlobal():
    global name
    name="Global Update"
    print("Name is : ",name)

if __name__ == '__main__':
    print("Name is : ",name) # global
    someFuntion() # local
    updateGlobal() # Global Update
#Output
    # Name is :  global
# Name is :  local
# Name is :  Global Update