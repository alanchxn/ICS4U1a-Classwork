while True:
    print("menu list...")
    
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("invalid choice")
        continue
    
    if choice == 0:
        print("Zero stuff")
    elif choice == 1:
        print("one stuff")
    elif choice == 2:
        print("two stuff")
    else:
        print("done")