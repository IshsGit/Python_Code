def has_pair_with_sum(numbers, k):
    seen = set()
    for num in numbers:
        complement = k - num
        if complement in seen:
            return True
        seen.add(num)
    return False


numbers = [10, 15, 3, 7]
k = 17
print(has_pair_with_sum(numbers, k))
