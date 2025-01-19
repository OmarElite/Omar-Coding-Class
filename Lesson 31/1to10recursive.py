def OnetoTen(count):
    print(count)
    count = count + 1

    if count <= 10:
        OnetoTen(count)
    else:
        return

OnetoTen(1)
