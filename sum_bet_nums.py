def get_sum(a, b):
    new_list = []
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        new_list.append(i)
        if a == b:
            return a
    return sum(new_list)


print(get_sum(0, 5))
