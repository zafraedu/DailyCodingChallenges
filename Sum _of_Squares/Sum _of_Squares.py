def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1)) # return n * (n + 1) * (2 * n + 1) // 6


# Tests
print(sum_of_squares(5))
print(sum_of_squares(10))
print(sum_of_squares(25))
print(sum_of_squares(500))
print(sum_of_squares(1000))