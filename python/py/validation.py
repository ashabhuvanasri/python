print("username validation")
username = input("Enter username: ")
if username.isalnum(): 
    print("Valid username") 
else: 
    print("Username should contain only letters and numbers")

print("password validation")
password = input("Enter password: ")
if len(password) >= 8: 
    print("Valid password") 
else: 
    print("Password should be at least 8 characters long")

print("email validation")
email = input("Enter email address: ")
if "@" in email and "." in email:
    print("Basic email format is valid") 
else: 
    print("Invalid email format")

print("strong validation")
password = input("Enter password: ") 
has_upper = False 
has_lower = False 
has_digit = False 
has_special = False 
for character in password: 
    if character.isupper(): 
        has_upper = True 
    elif character.islower(): 
        has_lower = True 
    elif character.isdigit(): 
        has_digit = True 
    else: 
        has_special = True 
if ( ): 
    len(password) >= 8 and has_upper and has_lower and has_digit and has_special 
    print("Strong Password") 
else:
    print("Weak Password")

print("phone number validation")
mobile = input("Enter mobile number: ") 
if mobile.isdigit() and len(mobile) == 10:
    print("Valid Mobile Number") 
else: 
    print("Invalid Mobile Number")

print("name validation")
name = input("Enter your name: ").strip() 
if name.replace(" ", "").isalpha():
    print("Valid Name") 
else:
    print("Name should contain letters only")