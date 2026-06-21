import numpy as np

# File Handling
def save_history(operation, result):
    with open("history.txt", "a") as file:
        file.write(f"{operation} = {result}\n")


# Basic Operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


# Statistical Operations
def statistics_calculator():
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))

    arr = np.array(numbers)

    print("\nStatistics Results")
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Variance:", np.var(arr))
    print("Maximum:", np.max(arr))
    print("Minimum:", np.min(arr))
    print("Sum:", np.sum(arr))

    save_history("Statistics", arr)



# Array Operations
def array_operations():
    numbers = list(map(float, input("Enter array elements separated by space: ").split()))

    arr = np.array(numbers)

    print("\nArray Operations")
    print("Original Array:", arr)
    print("Squared Array:", arr ** 2)
    print("Square Root:", np.sqrt(arr))
    print("Sum:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Sorted Array:", np.sort(arr))

    save_history("Array Operations", arr)


# Matrix Operations
def matrix_operations():

    print("\nEnter a 2x2 Matrix")

    a = float(input("A11: "))
    b = float(input("A12: "))
    c = float(input("A21: "))
    d = float(input("A22: "))

    matrix = np.array([[a, b],
                       [c, d]])

    print("\nMatrix:")
    print(matrix)

    print("\nTranspose:")
    print(matrix.T)

    print("\nDeterminant:")
    print(np.linalg.det(matrix))

    try:
        print("\nInverse:")
        print(np.linalg.inv(matrix))
    except:
        print("Inverse does not exist")

    save_history("Matrix", matrix)



# Main Program
while True:

    print("\n==============================")
    print(" AI & Data Science Calculator ")
    print("==============================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Statistics Calculator")
    print("8. Array Operations")
    print("9. Matrix Operations")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "10":
        print("Thank You!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print("Result:", result)

            elif choice == "2":
                result = subtract(num1, num2)
                print("Result:", result)

            elif choice == "3":
                result = multiply(num1, num2)
                print("Result:", result)

            elif choice == "4":
                result = divide(num1, num2)
                print("Result:", result)

            elif choice == "5":
                result = power(num1, num2)
                print("Result:", result)

            elif choice == "6":
                result = modulus(num1, num2)
                print("Result:", result)

            save_history("Basic Operation", result)

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "7":
        statistics_calculator()

    elif choice == "8":
        array_operations()

    elif choice == "9":
        matrix_operations()

    else:
        print("Invalid Choice")
