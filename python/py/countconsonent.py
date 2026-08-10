
text = input("Enter text: ").lower() 
vowels = "aeiou" 
count = 0 
for character in text: 
    if character.isalpha() and character not in vowels: count += 1 
print("Consonant Count:", count)



print("count digits")
text = input("Enter text: ").lower() 
vowels = "aeiou" 
count = 0 
for character in text: 
    if character.isdigit(): 
        count += 1 
print("Digit Count:", count)


print("count special characters")
text = input("Enter sentence: ") 
count = 0
for character in text:
    if character == " ":
        count += 1
print("Space Count:", count)

print("count uppercase and lowercase letters")
text = input("Enter text: ") 
uppercase_count = 0 
lowercase_count = 0 
for character in text: 
    if character.isupper(): 
        uppercase_count += 1 
    elif character.islower(): 
        lowercase_count += 1 
print("Uppercase Count:", uppercase_count) 
print("Lowercase Count:", lowercase_count)