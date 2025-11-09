try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    # for dividing a number by zero
    print("You cannot divide by zero")
except ValueError:
    # for when the data type is wrong
    print("Please enter a valid number.")
else:
    print("No error occurred.")
finally:
    print("This always runs.")