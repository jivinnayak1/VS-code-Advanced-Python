def shutdown(input):
    if input == "yes":
        return "shutting down"
    elif input == "no":
        return "abort shut down"
    else:
        return "sorry"


print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("maybe"))
