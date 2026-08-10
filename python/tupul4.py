
t = tuple(range(1, 11))
print(t)

t1= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("tuple")
print(t1)

print("length of tuple")
print(len(t1))

print("first element")
print(t1[0])

print("last element")
print(t1[-1])

print("three element")
print(t1[2])

print("three elements by slicing")
print(t1[1:4])

print("2 to 6 elements by slicing")
print(t1[2:6])

print("last three elements by slicing")
print(t1[-3:])

print("first three elements by slicing")
print(t1[0:3])

print("all elements except first element by slicing")
print(t1[1:])

print("all elements except last element by slicing")
print(t1[:-1])

print("reverse the tuple using slicing")
print(t1[::-1])

print("print alternate elements by slicing")
print(t1[::2])

print("print elements at even index by slicing")
print(t1[::2])

print("print elements at odd index by slicing")
print(t1[1::2])

print("find the index of an element")
print(t1.index(5))

print ("check whether an element exists in the tuple")
print(5 in t1)

t2 = (1, 2, 2, 3, 3, 3)
print("repeated tuple")
print(t2)
print("count of 2")
print(t2.count(2))
print("count of 3")
print(t2.count(3))

print("find the index of an element")
t3=("python", "java", "c++")
print(t3.index("python"))

t4=(1,10,4,2,10,5,6,10)
print(t4.count(10))

print("first occurrence of an element")
print(t2.index(3))

print("check whether java in a tuple")
print("java" in t3)

print("concatenate two tuples")
t5 = t1 + t3
print(t5)

print("repeat a tuple")
t6 = t3 * 3
print(t6)

print("convert a list to a tuple")
l1 = [1, 2, 3, 4, 5]
t7 = tuple(l1)
print(t7)

print("find the type")
print(type(t7))

print("convert a tuple to a list")
l2 = list(t7)
print(l2)
print("find the type")
print(type(l2))

print("add a new element to a tuple by creating a new tuple")
t8 = t7 + (6,)
print(t8)

print("remove an element from a tuple by converting into a list")
l3 = list(t8)
l3.remove(6)
t9 = tuple(l3)
print(t9)

print("replace an element in a tuple by converting into a list")
l4 = list(t9)
l4[0] = 100
t10 = tuple(l4)
print(t10)

print("create a tuple from user input values")
user_input = input("Enter values separated by spaces: ")
values = user_input.split()
t11 = tuple(values)
print(t11)

print("create a tuple using tuple() constructor")
t12 = tuple([1, 2, 3, 4, 5])
print(t12)

print("create a tuple of characters to a string using tuple() constructor")
t13 = tuple("hello")
print(t13)

print("maximum value in a tuple")
print(max(t1))

print("minimum value in a tuple")
print(min(t1))

print("sum of all elements in a tuple")
print(sum(t1))

print("find the average of all elements in a tuple")
print(sum(t1) / len(t1))

print("sort a tuple in ascending order")
print(sorted(t10))

print("sort a tuple in descending order")
print(sorted(t1, reverse=True))

print("second largest element in a tuple")
print(sorted(t1, reverse=True)[1])

print("second smallest element in a tuple")
print(sorted(t1)[1])

print("difference between max and min in a tuple")
print(max(t1) - min(t1))

print("create a tuple with student names")
t14 = ("Alice", "Bob", "Charlie", "David", "Eve")
print("print it by using for loop")
for student in t14:
    print(student)  

print("createa tuple with numbers")
t15 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("print even numbers")
for num in t15:
    if num % 2 == 0:
        print(num)
print("print odd numbers")
for num in t15:
    if num % 2 != 0:
        print(num)  

print("create a tuple with  student names and marks and courses")
t16 = (("Alice", 85, "Python"), ("Bob", 90, "Java"), ("Charlie", 75, "C++"))
print("print it by using for loop")
for student in t16:
    name, marks, course = student
    print(f"Name: {name}, Marks: {marks}, Course: {course}")              
