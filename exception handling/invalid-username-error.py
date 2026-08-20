class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter username: ")

    if not username:
        raise InvalidUsernameError("Username cannot be empty")

    print("Valid username")

except InvalidUsernameError as e:
    print("Error:", e)