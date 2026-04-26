# inventory system (products and prices)

# lists (arrays)
products = ["Milk", "Bread", "Eggs", "Sugar"]
prices = [75.0, 50.0, 9.0, 45.0]

# show all products
def show_products():
    print("\n==========================")
    print("       PRODUCT LIST       ")
    print("==========================")
    for i in range(len(products)):      # loop through list
        print(f"{i+1}. {products[i]:<10} ₱{prices[i]:.2f}")
    print("==========================")

# search product
def search():
    name = input("Enter product name to search: ")
    name = name.capitalize()
    print("--------------------------")
    if name in products:
        i = products.index(name)        # finds index
        print(f"FOUND ✅ {products[i]} - ₱{prices[i]:.2f}")
    else:
        print("❌ Product not found.")
    print("--------------------------")

# update price
def update():
    name = input("Enter product name to update: ")
    name = name.capitalize()
    print("--------------------------")
    if name in products:
        try:
            newp = float(input("Enter new price: "))
            i = products.index(name)
            prices[i] = newp            # update item price
            print("✅ Price updated successfully!")
        except:
            print("❌ Invalid price input!")
    else:
        print("❌ Product doesn't exist!")
    print("--------------------------")

# delete a product (extra feature)
def delete_product():
    name = input("Enter product name to delete: ")
    name = name.capitalize()
    print("--------------------------")
    if name in products:
        i = products.index(name)
        products.pop(i)                 # remove from lists
        prices.pop(i)
        print("🗑️ Product deleted!")
    else:
        print("❌ Product not found!")
    print("--------------------------")

# show total price (extra feature)
def total_value():
    print("--------------------------")
    print("Total inventory value: ₱", sum(prices))
    print("--------------------------")

# menu loop
while True:
    print("\n========= INVENTORY MENU =========")
    print("1. Show Products")
    print("2. Search Product")
    print("3. Update Price")
    print("4. Delete Product")
    print("5. Show Total Value")
    print("6. Exit")
    print("==================================")

    try:
        ch = int(input("Choose an option (1-6): "))

        if ch == 1:
            show_products()
        elif ch == 2:
            search()
        elif ch == 3:
            update()
        elif ch == 4:
            delete_product()
        elif ch == 5:
            total_value()
        elif ch == 6:
            print("Goodbye! 👋")
            break                       # stops program
        else:
            print("⚠️ Choose 1-6 only!")
    except:
        print("⚠️ Enter a number only!")
