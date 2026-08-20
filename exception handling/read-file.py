try:
    file = open("sample.txt", "r")
    data = file.read()

except FileNotFoundError:
    print("File not found")

else:
    print("File content:")
    print(data)

finally:
    print("File operation completed")