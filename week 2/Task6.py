def all_eq(lst):
    if not lst:
        return []
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    res = []
    for s in lst:
        padded = s.ljust(max_len, '_')
        res.append(padded)
    return res
