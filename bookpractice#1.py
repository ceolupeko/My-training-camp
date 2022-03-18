# Demonstration of linear and binary search

target = "c"
values = ["a", "b", "c", "d", "e", "f", "g", "h", "k", "l"]

# Linear search O(n)
for pointer in range(len(values)):
    if values[pointer] == target:
        print(pointer)

# Binary search O(log n)
left = -1
right = len(values)
while right > left + 1:
    mid = (left + right) // 2
    if values[mid] >= target:
        right = mid

    else:
        left = mid

print(right)
