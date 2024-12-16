def isArmstrong(number):

    num_string = str(number)
    num_digits = len(num_string)

    armstrong = sum(int(digit) ** num_digits for digit in num_string)

    return True if (number == armstrong) else False

print(isArmstrong(9474))