def fibonacci_sequence(start_sequence: list, length: int) -> list:
    if length == 0:
        return []
    if length == 1:
        return [start_sequence[0]]

    sequence = start_sequence[:2]

    while len(sequence) < length:
        sequence.append(sequence[-2] + sequence[-1])

    return sequence

print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))