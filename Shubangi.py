import math
def Power_Of_2(n):
    if n<=0:
        print("Invalid Input")
        return False
    if (math.log2(n).is_integer()):
        print("This is a power of 2")
    else:
        print("This isn't a power of 2")

Power_Of_2(14)