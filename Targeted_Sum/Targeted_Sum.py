def find_target(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return "Target not found"


# Tests
print(find_target([2, 7, 11, 15], 9))
print(find_target([3, 2, 4, 5], 6))
print(find_target([1, 3, 5, 6, 7, 8], 15))
print(find_target([1, 3, 5, 7], 14))