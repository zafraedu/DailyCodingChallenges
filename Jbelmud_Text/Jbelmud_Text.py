def jbelmu(text: str) -> str:
    words = text.split()
    result = []

    for word in words:
        if len(word) > 2:
            word = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
        result.append(word)

    return ' '.join(result)


# Tests
print(jbelmu("hello world"))
print(jbelmu("i love jumbled text"))
print(jbelmu("freecodecamp is my favorite place to learn to code"))
print(jbelmu("the quick brown fox jumps over the lazy dog"))