# Make functions to store the numbers ,sum,minus,multiply and divide
# Use while true to make sure the main menu keep on rerunning
while True:
    Menu = input("\n1.This is to calculate:\n2.This is all your calculations:\n3.Exit:\nEnter the number you want to see: ")
    def sum(number1,number2):
        return number1 + number2

    def minus(number1,number2):
        return number1 - number2

    def multi(number1,number2):
        return number1 * number2

    def divide(number1,number2):
        return number1/number2
    # Make function to ask user for there input
    def calculate():
        # Use while loop just in case the user want to make another calculation
        # Use try and except to make sure the user enters a number and not a letter
        while True:
            try:
                number1 = int(input("Please enter a number: "))
                number2 = int(input("Please enter a number: "))
            except ValueError:
                print("Error retry")
                continue
            # Ask user for the sum,minus,divide
            opert = input("What would you like to do (+,-,*,/): ")
            # Use if and elif statements to make sure you get the anwser of the numbers the user input
            if opert == "+":
                answer = sum(number1,number2)
                print(f" The is your sum: {answer}")
            elif opert == "-":
                answer = minus(number1,number2)
                print(f"The is your minus: {answer}")
            elif opert == "*":
                answer = multi(number1,number2)
                print(f"This is your multiply: {answer} ")
            elif opert == "/":
                answer = divide(number1,number2)
                print(f"This is your divide: {answer}")
# open the file and append all your calculation to the file
            with open("output.txt","a") as file:
                file.write("\n"+str(number1)+" "+opert+" "+str(number2)+" "+ "="+" "+str(answer))
# after the user got his anwser return to main menu
                return Menu
# make a function to view all calculations
    def view_all_calc():
# Use users input to read from the file and use try and except to make sure the users use the corrcet file name
        output = input("Do you want to view all calculations?  if so enter the file name: ").lower()
        try:
            with open(output,"r+") as file:
                for line in file.readlines():
                    print(f"This is your calculation: {line}")
        except FileNotFoundError as error:
            print("This file does not exist")
            print(error)

# Make a function to exit and use exit() to exit the loop
    def Exit():
        print("You have exited the calculator")
        exit()
# Use if statement to make sure you call whatever the user ask for
    if Menu == "1":
        calculate()
    if Menu == "2":
        view_all_calc()
    if Menu == "3":
        Exit()




