try:
    attendance = float(input("Enter attendance percentage: "))

    if attendance < 75:
        raise ValueError("Attendance is below 75%")

    print("Student is eligible")

except ValueError as e:
    print("Error:", e)