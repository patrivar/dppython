def laske(luku):
    result = True
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return result