def nth_fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b

# Tests
print(nth_fibonacci(4))
print(nth_fibonacci(10))
print(nth_fibonacci(15))
print(nth_fibonacci(40))
print(nth_fibonacci(75))
