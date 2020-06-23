def data_reverse(data):
    n = 8
    x = [data[i:i + n] for i in range(0, len(data), n)]
    x.reverse()
    j = sum(x, [])
    return j




print(data_reverse([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]))
