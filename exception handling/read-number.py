try:
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                number = int(line.strip())
                print(number)
            except ValueError:
                print("Invalid number:", line.strip())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")