mainMenu_list = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]

inventory = {
    "apple": {"price": 0.99, "stock": 100},
    "pear": {"price": 0.99, "stock": 100},
    "milk": {"price": 2.99, "stock": 50},
    "bread": {"price": 2.49, "stock": 75},
}
total_balance = 10000.0
system_running = True
operation_collection = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

while system_running:
    print("------Welcome to Main Menu------")
    for list in mainMenu_list:
        print(list)

    action = input("\nCommand:\n")

    # 'end': Terminate the program.
    if action == "end":
        system_running = False
        print("\n-----System Exit-----\n")

    # 'balance': The program should prompt for an amount to add or subtract from the account.
    elif action == "balance":
        print("------Balance------")
        add_money = float(input("How much you want to add or subtract from the account: "))
        total_balance += add_money
        print(f">>>>>Current Balance : {total_balance} <<<<<\n")
        if total_balance <= 0:
            print("***Warning: no enough balance***")
        operation_collection.append(">>>balance<<<")

    # 'sale': The program should prompt for the name of the product, its price, and quantity.
    # Perform necessary calculations and update the account and warehouse accordingly.
    elif action == "sale":
        print("------Sale------")
        sale_name = input("Enter product name: ")
        # check if product exist in inventory
        if sale_name in inventory.keys():
            sale_price = float(input("Enter price: "))
            # verify if input is positive
            if sale_price > 0:
                sale_quantity = int(input("Enter quantity: "))
                sale_money = sale_quantity * sale_price
                print(f"Amount of this transaction : {sale_money}")
                total_balance = total_balance + sale_money
                product_stock = inventory.get(f"{sale_name}").get("stock")
                inventory[sale_name]["stock"] = product_stock - sale_quantity
                if product_stock <= 0:
                    print(f"***Warning: no enough stocks for {sale_name}---current stock: {product_stock}***\n")

            else:
                print("***Error: input should be positive***\n")
        else:
            print(f"***{sale_name} not exist***\n")
        print(f">>>>>Current Balance : {total_balance} <<<<<\n")
        operation_collection.append(">>>sale<<<")

    # 'purchase': The program should prompt for the name of the product, its price, and quantity.
    # Perform necessary calculations and update the account and warehouse accordingly.
    # Ensure that the account balance is not negative after a purchase operation.
    elif action == 'purchase':
        print("------Purchase------")
        purchase_name = input("Enter product name: ")
        # check purchase product if already in warehouse
        if purchase_name in inventory.keys():
            purchase_price = float(input("Enter price: "))
            # verify if input is positive
            if purchase_price > 0:
                purchase_quantity = int(input("Enter quantity: "))
                purchase_money = purchase_price * purchase_quantity
                print(f"Amount of this transaction : {purchase_money}")

                product_stock = inventory.get(f"{purchase_name}").get("stock")

                inventory[purchase_name]["stock"] = product_stock + purchase_quantity

                total_balance = total_balance - purchase_money
                if total_balance <= 0:
                    print(f"***Warning: no enough balance --- current account balance : {total_balance}")
            else:
                print("***Error: input should be positive***\n")
            print(f">>>>>Current Balance : {total_balance} <<<<<\n")

        else:
            purchase_price = float(input("Enter price: "))
            # verify if input is positive
            if purchase_price > 0:
                purchase_quantity = int(input("Enter quantity: "))
                purchase_money = purchase_price * purchase_quantity
                print(f"Amount of this transaction : {purchase_money}")
                inventory[purchase_name] = {"price": purchase_price, "stock": purchase_quantity}
                print("***New product added***")

                total_balance = total_balance - purchase_money
                if total_balance <= 0:
                    print(f"***Warning: no enough balance --- current account balance : {total_balance}")

            else:
                print("***Error: input should be positive***\n")
            print(f">>>>>Current Balance : {total_balance} <<<<<\n")
            operation_collection.append(">>>purchase<<<")

    # Display the current account balance.
    elif action == "account":
        print("------Account------")
        print(f"Current account balance : {total_balance}")
        operation_collection.append(">>>account<<<")

    # 'list': Display the total inventory in the warehouse along with product prices and quantities.
    elif action == "list":
        print("---Inventory:--- ")
        for item, details in inventory.items():
            print(f"{item.capitalize()}: ")
            for detail, value in details.items():
                print(f"- {detail.capitalize()}: {value}")
        operation_collection.append(">>>list<<<")

    # 'warehouse': Prompt for a product name and display its status in the warehouse.
    elif action == "warehouse":
        print("------Warehouse------")
        product_name = input("Enter product name:")
        for item, details in inventory.items():
            if product_name == item:
                for detail, value in details.items():
                    print(f"- {detail.capitalize()}: {value}")
                break
        # else:
        print("***Product not exist***\n")
        operation_collection.append(">>>warehouse<<<")



    # 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range.
    # If ‘from’ and ‘to’ are empty, display all recorder operations.
    # Handle cases where 'from' and 'to' values are out of range.
    elif action == "review":
        print("------Review------")
        from_index = input("Enter 'from' indices: ")
        to_index = input("Enter 'to' indices: ")

        if not from_index and not to_index:
            print("Recorded operations:")
            for i in range(0, len(operation_collection)):
                print(">>>" + operation_collection[i] + "<<<")
        else:

            if int(from_index) < 0 or int(to_index) >= len(operation_collection) or int(from_index) > int(to_index):
                print("***Invalid index range***")
            else:
                print("Recorded operations:")
                for i in range(int(from_index) - 1, int(to_index)):
                    print(">>>" + operation_collection[i] + "<<<")


    else:
        print("\n-----Invalid command-----\n")
