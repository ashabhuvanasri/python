print("Find the longest word in a sentence")
sentence = input("Enter sentence: ") 
words = sentence.split()
longest = max(words, key=len) 
print("Longest Word:", longest)
print("find the shortest word in a sentence")
shortest = min(words, key=len) 
print("Shortest Word:", shortest)
print("Total Words:", len(words))

print("convert to title case")
title = input("Enter course title: ") 
print(title.title())

print("URL slug creation")
title = "Python Full Stack Development Course"
slug = title.lower().replace(" ", "-") 
print(slug)

