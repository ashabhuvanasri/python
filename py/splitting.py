
courses = "Python,Java,Data Science" 
result = courses.split(",") 
print(result)
massage = "python is a programming language.pythonis easy to learn"
print("split by space:", massage.split(" "))
massage2="python-java-data science"
print("right split:", massage2.rsplit("-"))
massage3="""python 
java
data science"""
print("split by lines:", massage3.splitlines())

