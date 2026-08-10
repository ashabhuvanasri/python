print("extract numbers from string")
text = "Order123Amount5000" 
numbers = "" 
for character in text: 
    if character.isdigit(): 
        numbers += character 
print(numbers)

print("extract letters from string")

text = "Python123Programming456" 
letters = "" 
for character in text: 
    if character.isalpha(): 
        letters += character 
print(letters)

print("extract spaces from characters")
text = "Python Programming Course" 
spaces = "" 
for character in text: 
    if character == " ": 
        spaces += character 
print(spaces)