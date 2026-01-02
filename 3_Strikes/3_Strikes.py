def squares_with_three(n):
    return sum(1 for i in range(1, n + 1) if '3' in str(i * i))

# Tests
print(squares_with_three(1))
print(squares_with_three(10))
print(squares_with_three(100))
print(squares_with_three(1000))
print(squares_with_three(10000))
