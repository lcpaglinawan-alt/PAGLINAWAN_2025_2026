def options():
    print("\nChoose an option:")
    print("{1} Show me the data :3")
    print("{2} Add or change data :3")
    print("{3} Summarize the data :3")
    print("{4} Quit the program >:( ")
    print("note: rainbowfish r INFACT real")

fish_data = [
    ["Honey Gourami", 4.0],
    ["Neon Tetra", 12.0],
    ["Zebra Pleco", 3.0],
    ["Rainbowfish", 8.0]
]

print("Hello! Welcome to the fish program.")
answer = input("Do you want to continue? (Y/N): ").upper()

if answer == "Y":
    while True:
        options()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n Fish Data brochacho:")
            print("------------------------")
            print("Name        | Amount ")
            print("------------------------")
            for row in fish_data:
                print(f"{row[0]:<12} | {row[1]}")
            print("------------------------")

        elif choice == "2":
            name = input("Enter fish name: ")
            size = float(input("Enter fish amount of fish: "))
            fish_data.append([name, size])
            print(f"Added: [{name}, {size}]")

            print("\n Updated Fish Data :3 :")
            print("------------------------")
            print("Name        | Amount ")
            print("------------------------")
            for row in fish_data:
                print(f"{row[0]:<12} | {row[1]}")
            print("------------------------")


        elif choice == "3":
            amount = [row[1] for row in fish_data]
            total = sum(amount)
            average = total / len(amount)
            smallest = min(amount)
            largest = max(amount)
            smallest_fishes = [row[0] for row in fish_data if row[1] == smallest]
            largest_fishes = [row[0] for row in fish_data if row[1] == largest]
            print("\n Fish Data Summary:")
            print(f"Total amount of all fishes: {total}")
            print(f"Average amount of fish (idk why u would need this): {average:.2f} fishes")
            print(f"Smallest amount of fish: {smallest} fishes ({', '.join(smallest_fishes)})")
            print(f"Largest amount of fish: {largest} fishes ({', '.join(largest_fishes)})")

        elif choice == "4":
            print("Fishy-bye!")
            break

        else:
            print("Invalid choice bruh! Please pick 1–4.")
elif answer == "N":
    print("Goodbye!")
else:
    print("Please type [Y/N] bruh")
