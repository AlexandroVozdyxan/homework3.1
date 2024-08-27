first_number = int(input("Enter a first number: "))
action = input("Enter a calculation(+, -, *, /: ")
second_number = int(input("Enter a second number: "))
if action == "+":
    result = first_number + second_number
    print(result)
elif action == "-":
    result = first_number - second_number
    print(result)
elif action == "*":
    result = first_number * second_number
    print(result)
elif action == "/":
    if second_number == 0:
        print("Error")
    else:
        result = first_number / second_number
        print(result)