operators = ("+", "-", "*", "/", "**", "//")
for opr in operators:
    print(opr)
operation = input("press any operator to perform the operations : ")
number = int(input("Enter the numbers : "))
number1 = int(input("Enter the second no : "))
if operation == "+":
    print(number+number1)
    
elif operation == "-":
    print(number-number1)
    
elif operation == "*":
    print(number*number1)
    
elif operation == "/":
    print(number/number1)
    
elif operation == "**":
    print(number**number1)
    
elif operation == "//":
    print(number//number1)   
else: print("invalid operator")



