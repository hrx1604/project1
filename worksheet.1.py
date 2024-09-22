#Declare variables a and b
a = 15
b = 12

#Print the types of a and b
print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")


# Addition
add = a + b
print(f"Addition (a + b): {add}")

# Subtraction
sub = a - b
print(f"Subtraction (a - b): {sub}")

# Multiplication
mul = a * b
print(f"Multiplication (a * b): {mul}")

# Division
div = a / b
print(f"Division (a / b): {div}")

 
# Integer division result
c = a // b
print(f"Value of c (integer division): {c}")
print(f"Type of c: {type(c)}")

# Convert c to float
c_float = float(c)
print(f"Value of c as float: {c_float}")
print(f"Type of c as float: {type(c_float)}")


# String message
message = "The result of a divided by b is:"
# Concatenate message with the value of c converted to string
result = f"{message} {c}"
print(result)


# Compare if a is greater than b
is_a_greater = a > b
print(f"a > b: {is_a_greater}")

# Check if a is equal to b
is_a_equal_b = a == b
print(f"a == b: {is_a_equal_b}")
