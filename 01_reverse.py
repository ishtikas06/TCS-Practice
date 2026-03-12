arr = [1,2,3,4,5]

# arr = arr[::-1]
start, end = 0, len(arr)-1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)