def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def Multi(num1, num2):
    return num1 * num2


def DIV(num1, num2):
    return num1 / num2


def calc():
    print("Select Mode:")
    print("1. Add +")
    print("2. Subtract -")
    print("3. Multiply *")
    print("4. Divide /")

    mode = input("Enter Your Mode (1/2/3/4): ")
    number1 = float(input("Enter Your First Number: "))
    number2 = float(input("Enter Your Second Number: "))

    if mode == "1":
        print(add(number1, number2))
    elif mode == "2":
        print(sub(number1, number2))
    elif mode == "3":
        print(Multi(number1, number2))
    elif mode == "4":
        print(DIV(number1, number2))
    else:
        print("Invalid mode")


calc()
