num=int(input("Enter matrix: "))

for x in range (1, num +1):
    for y in range (1, num +1):
        if x%2==0:
            print(f"*", end=" ")
        else:
            print(f"*", end=" ")
    print()