def main():
    # Open a file for writing and create it if it doesn't exist
    f = open("textfile.txt", "w+")

    # add content
    addline(f)

    # Open the file for appending text to the end
    # f = open("textfile.txt","a+")
    # addline(f)

    # close the file when done
    f.close()

    # Open the file back up and read the contents
    f = open("textfile.txt", "r")
    if f.mode == 'r':  # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
        # print (contents)

        fl = f.readlines()  # readlines reads the individual lines into a list
        for x in fl:
            print(x)

# write some lines of data to the file
def addline(file):
    for i in range(10):
        file.write("This is line %d\r\n" % (i + 1))


if __name__ == "__main__":
    main()