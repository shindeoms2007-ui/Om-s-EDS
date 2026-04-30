def main():
    integer_list = []

    while True:

        print("1. Add")
        print("2. Remove")
        print("3. Display")
        print("4. Quit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 1:
            # Add
            try:
                num = int(input("Integer: "))
                integer_list.append(num)
                print(f"List after adding: {integer_list}")
            except ValueError:
                print("Invalid input")

        elif choice == 2:
            # Remove
            if not integer_list:
                print("List is empty")
            else:
                try:
                    num = int(input("Integer: "))
                    if num in integer_list:
                        integer_list.remove(num)
                        print(f"List after removing: {integer_list}")
                    else:
                        print("Element not found")
                except ValueError:
                    print("Invalid input")

        elif choice == 3:
            # Display
            if not integer_list:
                print("List is empty")
            else:
                print(integer_list)

        elif choice == 4:
            # Quit
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()