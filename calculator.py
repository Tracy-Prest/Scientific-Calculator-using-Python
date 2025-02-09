import math
# modified to scientific calculator


# enter the number option you want

print("\n Calculator number range 0 to 90 ")
print("\n Choose Option ")
number = print(" 1. Add \n","2. Subtract \n","3. Multiply \n","4. Divide \n", "5. Square root \n", "6. Sine \n", "7. Cos \n", "8. Tan \n")


# only numbers specific numbers can be used
while True:
    number = input("Type in option from 1 to 8: \n ")

    numbers = range(90)
    for option in numbers:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
        except ZeroDivisionError:
           print("Not divisible by 0")
           
        except ValueError:
            print("Invalid input. Please enter a number within number range!")
            continue

        if number == "1":
          print(num1, "+", num2, "=" , num1 + num2)

        elif number == "2":
          print(num1, "-", num2 ,"=", num1 - num2)

        elif number == "3":
          print(num1, "*" , num2, "=" , num1 * num2)

        elif number == "4":
           try:
              print(num1, "/", num2, "=" , num1 / num2)
           except ZeroDivisionError:
              print("Cannot be divided by zero")
        # add square, sine, cos, tan use math functions
        elif number == "5":
           print(f"To get square root, enter {num2==0}")
           print(f"Square root of {num1} = {math.sqrt(num1)}" )
        elif number == "6":
           print(f"To get sine, enter {num2==0} 0")
           print(f"Sine {num1} = {math.sin(num1)}")
        elif number == "7":
           print(f"To get cosine, enter {num2==0}")
           print(f"Cos {num1} = {math.cos(num1)}")
        elif number == "8":
           print(f"To get tan, enter {num2==0}")
           print(f"Tan {num1} = {math.tan(num1)}")
          
        
    
# ask if there will be another calculation
        another_calculation = input("Do you want another calcultaion with same operator? (yes/no): \n")
        if another_calculation == "no":
            break
        