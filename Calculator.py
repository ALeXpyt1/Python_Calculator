import random
offers = [
    "Let's count again!",
    "Enter what needs to be calculated!",
    "Are you going to the next example?",
    "What do we counted next?"
]
print("Welcome to Calculator!")
start = input("Do you want to start? (yes/no): ")
if start == "Yes" or start == "yes":
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /, %, //, **): ")
        if operation == "+":
            print("Result: ", num1 + num2)
        elif operation == "-":
            print("Result: ", num1 - num2)
        elif operation == "*":
            print("Result: ", num1 * num2)
        elif operation == "/":
            if num1 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error.You can't divide by zero!")
        elif operation == "%":
            print(" Result: ", num1 % num2)
        elif operation == "//":
            print("Result: ", num1 // num2)
        elif operation == "**":
            print("Result: ", num1 ** num2)
        else:
            print("Invalid operation, please try again")

        again = input("Do you want to continue? (yes/no): ")
        if again == "Yes" or again == "yes":
            print(random.choice(offers))
            continue
        elif again == "No" or again == "no":
            print("Goodbye! See you next time!")
            break
        else:
            print("Invalid operation, please try again")

elif start == "No" or start == "no":
    print("Goodbye! See you next time!")
else:
    print("Invalid operation, please try again")



