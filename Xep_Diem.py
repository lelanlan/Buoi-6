def take_secon(elemm):
    return elemm[2]

random =[(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1),(9,8,6)]
sorted_list = sorted(random, key=take_secon)
print('List đã được sắp xếp:', sorted_list)

