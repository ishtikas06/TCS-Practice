arr = [1,2,3,4,5]

max = arr[0]

first = sec = float("-inf")

for elem in arr:
    if elem > first:
        sec = first
        first = elem
    elif elem > sec and elem != first:
        sec = elem

print(sec)