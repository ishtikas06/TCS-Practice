arr = [1,2,3,4,5]
k = 2
k = k % len(arr)

# # right rotate
# arr = arr[-k:] + arr[:-k]
# print(arr)

# arr = [1,2,3,4,5]
# # left rotate
# arr = arr[k:] + arr[:k]

def rotate(arr, k):
    n = len(arr)
    k = k % n

    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])

    return arr

print(rotate(arr, 2))