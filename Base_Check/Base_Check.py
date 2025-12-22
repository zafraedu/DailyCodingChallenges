def is_valid_number(s: str, base: int) -> bool:
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_chars = set(digits[:base])

    return all(char.upper() in valid_chars for char in s)

# Tests
print(is_valid_number("10101", 2)) # True
print(is_valid_number("10201", 2)) # False
print(is_valid_number("76543210", 8)) # True
print(is_valid_number("9876543210", 8)) # False
print(is_valid_number("9876543210", 10)) # True
print(is_valid_number("ABC", 10)) # False
print(is_valid_number("ABC", 16)) # True
print(is_valid_number("Z", 36)) # True
print(is_valid_number("ABC", 20)) # True
print(is_valid_number("4B4BA9", 16)) # True
print(is_valid_number("5G3F8F", 16)) # False
print(is_valid_number("5G3F8F", 17)) # True
print(is_valid_number("abc", 10)) # False
print(is_valid_number("abc", 16)) # True
print(is_valid_number("AbC", 16)) # True
print(is_valid_number("z", 36)) # True
