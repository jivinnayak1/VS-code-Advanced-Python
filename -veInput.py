def take_input_recursively():
    
    number = int(input("Enter your number: "))
    
    if number < 0:
        print("Number -ve")
        return
    else:
        print("Number +ve")
        take_input_recursively()
take_input_recursively()
