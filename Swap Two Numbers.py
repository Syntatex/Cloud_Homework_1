# Program to swap two numbers

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Printing original values
print("\nBefore swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swapping the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Printing swapped values
print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
