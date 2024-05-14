def check_palindrome(strInput):
    temp = strInput.lower()

    # strip all spaces and punctuations
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c

    # reverse a string
    reverseStr = ""
    strindx = len(newstr) - 1
    while (strindx >= 0):
        reverseStr += newstr[strindx]
        strindx -= 1

    # Compare strings
    if newstr == reverseStr:
        return True
    return False


print(check_palindrome("Hello"))#False
print(check_palindrome("Radar"))#True
print(check_palindrome("Mama?"))#False
print(check_palindrome("I'm Adam."))#False
print(check_palindrome("Race car!"))#True

# test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",    "Race car!"]
