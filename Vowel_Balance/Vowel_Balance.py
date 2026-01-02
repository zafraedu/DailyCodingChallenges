def is_balanced(s: str) -> bool:
    vowel = set('aeiouAEIOU')
    mid = len(s) // 2

    left = s[:mid]
    right = s[-mid:]

    count_vowel_left = sum(1 for l in left if l in vowel)
    count_vowel_right = sum(1 for l in right if l in vowel)

    return count_vowel_left == count_vowel_right


# Tests
print(is_balanced("racecar"))
print(is_balanced("Lorem Ipsum"))
print(is_balanced("Kitty Ipsum"))
print(is_balanced("string"))
print(is_balanced(" "))
print(is_balanced("abcdefghijklmnopqrstuvwxyz"))
print(is_balanced("123A#b!E&*456-o.U"))
