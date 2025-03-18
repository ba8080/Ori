# This app is used to mange my budget

budget_data = {
 "balance": 500,
 "transactions": [
 {"type": "income", "amount": 1000, "description": "Salary"},
 {"type": "expense", "amount": 500, "description": "Groceries"}
 ]
}


def add_transaction(budget_data, type, amount, description=""):
    # Add the transaction to the list of transactions
    budget_data["transactions"].append({
        "type": type,
        "amount": amount,
        "description": description
    })

    # Update the balance based on the transaction type
    if type == "income":
        budget_data["balance"] += amount
    elif type == "expense":
        budget_data["balance"] -= amount
    else:
        print("Invalid transaction type. Please use 'income' or 'expense'.")

    return budget_data




# main.py

def main_menu():
    while True:
        print("\nStore Inventory Management Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                quantity = int(input("Enter Income ammount: "))
            case '2':
                name = input("Enter product name to remove: ")
                im.remove_product(name)
            case '3':
                name = input("Enter product name to update: ")
                field = input("Update (q)uantity or (p)rice? ")
                if field == 'q':
                    quantity = int(input("Enter new quantity: "))
                    im.update_product(name, quantity=quantity)
                elif field == 'p':
                    unit_price = float(input("Enter new unit price: "))
                    im.update_product(name, unit_price=unit_price)
            case '4':
                im.display_inventory()
            case '5':
                im.calculate_total_value()
            case '6':
                im.most_expensive_product()
            case '7':
                print("Exiting program.")
            case '8':
                im.showinv()
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()