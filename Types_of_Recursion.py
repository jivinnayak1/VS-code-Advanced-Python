#Tail Recursion
def tail(n):
    if (n!=0):
        print(n)

        tail(n-1)
x = 4

tail(x)

print("")

#Head Recursion
def head(n):
    if(n!=0):
        head(n-1)

        print(n)
x = 5

head(x)

print("")

#Tree Recursion
def tree(n):
    if (n!=0):
        print(n)
        tree(n-1)
        tree(n-1)
tree(3)