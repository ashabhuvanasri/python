def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found"

    except PermissionError:
        return "Permission denied"


filename = input("Enter filename: ")

print(read_file(filename))