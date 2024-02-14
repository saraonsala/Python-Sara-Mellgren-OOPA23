
try:
    num = int(input(f"Choose a number,then I'll tell you if it's positive or negative: "))

    if num <= 1:
        print("Your number is negative")
    elif num ==0 :
        print(" Your number is zero")
    else:
        print ("Your number is positive")

except ValueError:
    print("Invalid entry. Please enter a valid number.")
