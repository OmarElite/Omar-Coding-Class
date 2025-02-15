def TowerOfHanoi(n, a, b, c): # n is  the number of Disk, a is the first Rod(The Origine), b is the last Rod(The Destination), c is the helper Rod
    if n == 1:
        print(f"Move disk 1 from Rod {a} to Rod {b}")
        return
    
    # Move n - 1 disk from a to b
    TowerOfHanoi(n-1, a, c, b)

    print(f"Move disk {n} from Rod {a} to Rod {b}")
    TowerOfHanoi(n-1, c, b, a)

n = 4
TowerOfHanoi(n, "A", "C", "B")
