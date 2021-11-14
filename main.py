def merge(*lists):
    result = []
    for l in lists:
        result.extend(l)
    result.sort()
    return result