# Examples of different number types
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print(type(integer_num))
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")
print()

# Basic Arithmetic Operations
a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Floor Division: {a} // {b} = {a // b}") # Floor division returns the largest integer less than or equal to the division result.
print(f"Modulus: {a} % {b} = {a % b}")
print()

# Operator Precedence
# Python Operator Precedence (Highest to Lowest):
# 1. Parentheses `()`: Used to group expressions and override the default precedence.
# 2. Exponentiation `**`: Right-to-left associativity.
# 3. Unary Operators: `+`, `-`, `~` (positive, negative, bitwise NOT).
# 4. Multiplicative Operators: `*`, `/`, `//`, `%` (multiplication, division, floor division, modulus).
# 5. Additive Operators: `+`, `-` (addition, subtraction).
# 6. Bitwise Shift Operators: `<<`, `>>` (left shift, right shift).
# 7. Bitwise AND: `&`
# 8. Bitwise XOR: `^`
# 9. Bitwise OR: `|`
# 10. Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`.
# 11. Logical NOT: `not`
# 12. Logical AND: `and`
# 13. Logical OR: `or`
# 14. Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, etc.
# 15. Expression Separators: `,`

# Example code demonstrating precedence:
a = 5
b = 2
c = 3

# Parentheses override precedence
print((a + b) * c)  # Parentheses take highest precedence

# Exponentiation
print(a ** b)  # Exponentiation (5^2 = 25)

# Multiplicative and Additive
print(a + b * c)  # Multiplication has higher precedence than addition

# Logical Operators
print(a > b and b < c)  # Comparison happens before logical AND

# Bitwise Operations
print(a & b | c)  # Bitwise AND happens before Bitwise OR
print()

