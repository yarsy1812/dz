nesort = [12, 4, 9, 1, 6, 3]
print(nesort)

psort = []
for x in nesort:
    psort.append([x])

while len(psort) > 1:
    left = psort[0]
    psort.remove(left)
    
    right = psort[0]
    psort.remove(right)
    
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])
            
    while len(left) > 0:
        merged.append(left[0])
        left.remove(left[0])
        
    while len(right) > 0:
        merged.append(right[0])
        right.remove(right[0])
        
    psort.append(merged)

sort = psort[0]
print(sort)
