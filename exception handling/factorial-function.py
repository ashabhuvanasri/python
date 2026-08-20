def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial cannot be negative")

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

    except ValueError as e:
        return str(e)


try:
    number = int(input("Enter number: "))
    print("Factorial:", factorial(number))

except ValueError:
    print("Invalid input")