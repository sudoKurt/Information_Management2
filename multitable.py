while True:

    rows = int(input("Enter row: "))
    cols = int(input("Enter col: "))

    if rows <= 0 or cols <= 0:
        search = int(input("Search: "))
        print("stop the loop")
        break

    search = int(input("Search: "))

    print("\nOutput:")

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            value = i * j
            if value == search:
                print(f"[{value}]", end=" ")
            else:
                print(value, end=" ")
        print()
    print()  