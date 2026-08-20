def get_element(numbers, index):
    try:
        return numbers[index]

    except IndexError:
        return "Index out of range"


numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(get_element(numbers, index))

except ValueError:
    print("Invalid index")