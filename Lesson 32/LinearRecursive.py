def LinearRec(count):
    if count > 1:
        return
    
    print("Hello")
    count = count + 1 
    LinearRec(count)

LinearRec(1)
