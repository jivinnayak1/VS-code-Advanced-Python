Tickets = [4,34,3,49,23,65,21]

Book = int(input("Which Seat Number Would You Like to Book: "))


if Book in Tickets:
        print("Already Booked. Please Book Another Ticket45")
else:
        print("Tickets have been booked succesfully")
        Tickets.append(Book)