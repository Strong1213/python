# Python Functions Example

# 1. Function without parameter and return
def greet():
    print("Hello! Welcome to Python functions.")

# 2. Function with parameter
def greet_user(name):
    print(f"Hello, {name}!")

# 3. Function with return value
def add_numbers(a, b):
    return a + b

# 4. Function with default parameter
def power(base, exp=2):
    return base ** exp

# 5. Function with variable arguments (*args)
def total_sum(*numbers):
    return sum(numbers)


# ----------------------
# Function calls
# ----------------------
greet()

greet_user("Raza")

result = add_numbers(10, 20)
print("Sum of 10 and 20:", result)

print("5 squared:", power(5))
print("2 to the power 5:", power(2, 5))

print("Total sum of 1,2,3,4,5:", total_sum(1, 2, 3, 4, 5))
