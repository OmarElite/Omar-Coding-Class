def Dream(count):
    count = count + 1
    print("Dreaming")

    if count < 10:
        Dream(count)
    else:
        exit

Dream(0)
