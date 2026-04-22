#simple calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
choice=input("Enter operation (+, -, *, /): ")
if choice == '+':
    print("Result:", num1 + num2)
elif choice == '-':
    print("Result:", num1 - num2)   
elif choice == '*':
    print("Result:", num1 * num2)
elif choice == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operation")


    
