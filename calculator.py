
# display opitions to user
# take user input
    # if user input = x then
            #preform operation

def menu():
    print("Calculator Menu")

    print("1) Add")
    print("2) Subtract")
    print("3) Multipy")
    print("4) Divide")

    choice = input("Please select an operation: ")

    #if (1+1):
    #   print("True") 
    #else:
    #    print("False")


    if (choice == "1"):
        num_1 = get_number()
        num_2 = get_number()

        add(num_1, num_2)

    elif (choice == "2"):
        num_1 = get_number()
        num_2 = get_number()

        subtract(num_1, num_2)

    elif (choice == "3"):
        num_1 = get_number()
        num_2 = get_number()

        multipy(num_1, num_2)

    elif (choice =="4"):
        num_1 = get_number()
        num_2 = get_number()

        divide(num_1, num_2)

    else:
        print("This option does not exist")

    menu()
    exit

# Function - returns a value
# Subroutine - just preforms, does not return value

def add(num_1, num_2):
    answer = num_1 + num_2

    print(num_1, " + ", num_2, " = ", answer)

def subtract(num_1, num_2):
    answer = num_1 + num_2

    print(num_1, " - ", num_2, " = ", answer)

def multipy(num_1, num_2):
    answer = num_1 + num_2

    print(num_1, " * ", num_2, " = ", answer)

def divide(num_1, num_2):
    answer = num_1 + num_2

    print(num_1, " / ", num_2, " = ", answer)

def get_number(): 

    try:
        number = int(input("Please enter a number:"))
        return number

    except Exception as ex:
        print("Please only enter a number")
        get_number()
        exit

menu()
exit
