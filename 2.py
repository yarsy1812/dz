list = [2, 5, 8, 11, 14, 18,  21, 25, 30]
val = 18
first = 0
last = len(list)-1
index = -1
while (first <= last) and (index == -1):
    mid = (first+last)//2
    if list[mid] == val:
        index = mid
    else:
        if val<list[mid]:
            last = mid -1
        else:
            first = mid +1
print(index)