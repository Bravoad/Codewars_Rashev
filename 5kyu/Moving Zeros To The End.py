def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = [x for x in arr if x == 0]
    return non_zeros + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))