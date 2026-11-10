nesort = [29, 10, 14, 37, 13]
print(nesort)
sort = []
while len(nesort) > 0:
    min = nesort[0]
    for i in range(0, len(nesort)):
        if nesort[i] < min:
            min = nesort[i]
    sort.append(min)
    nesort.remove(min)
    print(sort)

print(sort)