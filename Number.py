def Armstrong(number):
    num_str = str(number)
    l = len(num_str)
    sum=0

    for digit in num_str:
       sum = int(digit) ** l + sum

    return True if sum==number else False

print(Armstrong(153))
print(Armstrong(370))
print(Armstrong(944))

number = 12345
number_str = str(number)
digit_count = len(number_str)
print(digit_count)

987 = 9+8+7 = 24 = 2+4 = 6

def sum_until_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

number = 987
result = sum_until_single_digit(number)
print(f"The final single-digit sum of {number} is {result}.")

number = (int(input("Enter a number: ")))

if number % 2==0:
    print("Even")
else:
    print("Odd")