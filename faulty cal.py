def calculator():
    print("\nWellcome to python calculator with developer mezbah")
    operation = ("+","-","*","/","**","%")



    num1 = int(input("Enter first Number"))
    num2 = int(input("Enter your second Number"))

    if operation == '+':
        if num1 == 56:
            print("56 + 9 = 77")
        else:
            print("f*{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print("f{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        if num1 == 45:
            print("45*3 = 555")
        else:
            print("f{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num1 == 50:
            print("50/10 = 5")
        else:
            print("f{num1} / {num2} = {num1 / num2}")
    elif operation == '**':
        print("f{num1} ** {num2} = {num1 ** num2}")
    elif operation == '%':
        print("f{num1}%{num2} = {num1 %num2}")
    else:
        print("You press a invalid key")
    again()

def again():
    call_again = input('''Do you want to calculate again?
                        Please type y for yes or n for no.''')


    if call_again == 'y':
        calculator()
    elif call_again == 'n':
        print("See Ypu Later")
    else:
        again()

calculator()