mydict = {}

size = int(input('Matrix Size: ')) 

for i in range(size):

    value = input(f'Shopping Items {i+1}: ')   
    mydict[i] = value

print("You have", len(mydict), "items in the cart")

while True:
    choice = input("\nWhat would you like to do [C]hange  [R]emove  [D]isplay  S[earch]  [*]Exit: ").lower()

    if choice == "d":   
        print("Key   Value")
        for k, v in mydict.items():
            print(k, "   ", v)

    elif choice == "s":   
        item = input("\nEnter item to search: ")
        if item.isdigit():
            key = int(item)
            if key in mydict:
                print("Found:", mydict[key])
            else:
                print("Not in the cart")
        else:
            if item in mydict.values():
                print("Found:", item)
            else:
                print("Not in the cart")

    elif choice == "r":   
        key = input("Enter key to search: ")
        if key.isdigit():
            key = int(key)
            if key in mydict:
                print("Removed:", mydict[key])
                mydict.pop(key)
            else:
                print("Key not found")
        else:
            print("Key not found")

    elif choice == "c":   
        key = input("Enter key to search: ")
        if key.isdigit():
            key = int(key)
            if key in mydict:
                print("Current value:", mydict[key])
                mydict[key] = input("Enter new value: ")
            else:
                print("Key not found")
        else:
            print("Key not found")

    elif choice == "*":   # exit
        print("Bye")
        break

    else:
        print("Im sorry, not in the cart")