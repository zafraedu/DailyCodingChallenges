from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    clean_str1 = str1.replace(' ', '').lower()
    clean_str2 = str2.replace(' ', '').lower()
    return Counter(clean_str1) == Counter(clean_str2) # sorted() is also an option

# Tests
print(are_anagrams("listen", "silent"))
print(are_anagrams("School master", "The classroom"))
print(are_anagrams("A gentleman", "Elegant man"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("apple", "banana"))
print(are_anagrams("cat", "dog"))