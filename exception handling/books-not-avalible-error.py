class BookNotAvailableError(Exception):
    pass


books = ["Python", "Java", "C++"]

try:
    book = input("Enter book name: ")

    if book not in books:
        raise BookNotAvailableError("Book is not available")

    print("Book available")

except BookNotAvailableError as e:
    print("Error:", e)