arr = [2,2,1,3,1,1,3,1,2]

count = 0
candidate: int
for elem in arr:
    if count == 0:
        candidate = elem

    if elem == candidate:
        count += 1
    else:
        count -= 1

elem_count = 0
for elem in arr:
    if elem == candidate:
        elem_count += 1

if elem_count > len(arr)//2:

    print(candidate)

else:
    print("No majority element")