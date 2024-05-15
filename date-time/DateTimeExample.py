from datetime import date
from datetime import datetime


def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date Components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's Weekday #: ", today.weekday())
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("Which is a " + days[today.weekday()])

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is ", today)

    # Get the current time
    t = datetime.time(datetime.now())
    print("The current time is ", t)


if __name__ == "__main__":
    main()

# Output:
# Today's date is  2024-05-15
# Date Components:  15 5 2024
# Today's Weekday #:  2
# Which is a wednesday
# The current date and time is  2024-05-15 10:44:49.310986
# The current time is  10:44:49.310986