for x in range(6,1,-1):
    for y in range(6,1,-1):
        if x%y==0:
            x-=1  
            print(f"{x}", end=" ")
    print()