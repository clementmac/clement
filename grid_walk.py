def is_valid_walk(walk):
    hori = 0
    vert = 0
    count = len(walk)
    for dir in walk:
        if dir == 'n':
            vert += 1
        elif dir == 's':
            vert -= 1
        elif dir == 'e':
            hori += 1
        elif dir == 'w':
            hori -= 1
    if vert == 0 and hori == 0 and count == 10:
        return True
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))