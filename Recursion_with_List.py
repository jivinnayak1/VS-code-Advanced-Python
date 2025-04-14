#Normal Way:

# Numbers = [2,34,53,235,235,54,345,345,4356]
# print(Numbers)
# print(len(Numbers))

#Recursion Way:

def list_length_recursive(lst):
    if not lst:
        return 0
    return 1 + list_length_recursive(lst[1:])

example_list = [1, 2, 234, 234, 745, 3, 6, 653]
print("Length of array:", list_length_recursive(example_list))
