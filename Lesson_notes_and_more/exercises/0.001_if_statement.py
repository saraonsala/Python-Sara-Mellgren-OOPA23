
try:
    num1 = int(input(f"enter two numbers and I'll tell you which one is bigger: "))
    num2 = int(input(f"And now the seccond number: "))

    if num1 < num2:
        print("The smallest number is:",num2 )
    elif num1 > num2 :
        print(" The smallest number is:",num1)
    else:
        print ("Both numbers are equal.")

except ValueError:
    print("Invalid entry. Please enter a valid number.")
