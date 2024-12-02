medical_issue = input("Do ypu have any medical issues? (Answer Yes/No): ")

if medical_issue == "Yes":
    print("Eligible")
else:
     attendance = int(input("Enter you Attendance in Percent (example - 89): "))
     if attendance >=75:
          print("Eligible")
     else:
          print("Not Eligible")