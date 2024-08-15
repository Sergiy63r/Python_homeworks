lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
l = len(lst)

for y in range(0, l):
    if (y < 30) and (y % 3 == 0):
	    print(lst[y])

