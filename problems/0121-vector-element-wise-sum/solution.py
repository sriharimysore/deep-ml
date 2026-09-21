def vector_sum(a: list[int | float], b: list[int | float]) -> list[int | float] | int:
    # Different lengths cannot be added
    if len(a) != len(b):
        return -1

    list_3 = []
    q = len(a) - 1
    p = -1

    while p < q:
        p = p + 1
        x = a[p] + b[p]
        list_3.append(x)

    return list_3