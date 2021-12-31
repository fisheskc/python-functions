def do_calculation():
    print("Hi")
    print("I am a Maths Bot")
    bots_name = "Marvin"
    # The sentence and the bots name are added together for output
    print("My name is " + bots_name)
    # Ask for the user input here
    yourUser_math = input("How can we help? Can I help you add or subtract? ")
    # This checks against the user input for the list of instructions to follow
    print("lets " + yourUser_math + " some numbers")
    print("lets add some numbers")
    input1 = input("Number 1>")
    input2 = input("Number 2>")
    number1 = int(input1)
    number2 = int(input2)
    if yourUser_math == "add" or yourUser_math == "Add" or yourUser_math == "lets add" or yourUser_math == "let's add":
        result = number1 + number2
        output = str(result)
        print(input1 + " + " + input2 + " = " + output)
    elif yourUser_math == "minus" or yourUser_math == "subtract" or yourUser_math == "lets minus" or yourUser_math == "let's minus":
        print("Let me do some subtract for you")
        result = number1 - number2
        output = str(result)
        print(input1 + " - " + input2 + " = " + output) 
    else:
        print("Sorry, I could not help.")    
do_calculation()
