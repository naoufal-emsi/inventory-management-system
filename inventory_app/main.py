# main.py

from core.inventory_ops import *
from core.stock_monitor import *
from core.transaction_ops import *
from core.reports import *
from data.inventory_data import products
from datetime import datetime

def inventory_menu():
    while True:
        print("\n--- Inventory Operations ---")
        print("1. Add product")
        print("2. Update product")
        print("3. Delete product")
        print("4. Search product by name")
        print("5. Sort products by field")
        print("6. List all products")
        print("7. Back to main menu")
        choice = input("Select option: ")

        if choice == "1":
            pid = int(input("ID: "))
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            category = input("Category: ")
            add_product({"id": pid, "name": name, "price": price, "quantity": quantity, "category": category})
        elif choice == "2":
            pid = int(input("Product ID to update: "))
            field = input("Field to update (name/price/quantity/category): ")
            value = input("New value: ")
            if field in ["price", "quantity"]:
                value = float(value) if field == "price" else int(value)
            update_product(pid, {field: value})
        elif choice == "3":
            delete_product(int(input("Product ID to delete: ")))
        elif choice == "4":
            print(search_product_by_name(input("Search name: ")))
        elif choice == "5":
            print(sort_products_by(input("Sort by field (name/price/quantity/category): ")))
        elif choice == "6":
            print(list_all_products())
        elif choice == "7":
            break

def stock_menu():
    while True:
        print("\n--- Stock Monitoring ---")
        print("1. View low stock products")
        print("2. Auto restock")
        print("3. Calculate stock value")
        print("4. Inventory by category")
        print("5. Back to main menu")
        choice = input("Select option: ")

        if choice == "1":
            print(get_low_stock_products(int(input("Threshold: "))))
        elif choice == "2":
            auto_restock(int(input("Min level: ")), int(input("Restock to: ")))
        elif choice == "3":
            print("Total stock value:", calculate_stock_value())
        elif choice == "4":
            print(get_inventory_by_category())
        elif choice == "5":
            break

def transaction_menu():
    while True:
        print("\n--- Transactions ---")
        print("1. Sell product")
        print("2. Purchase product")
        print("3. View transaction history")
        print("4. Back to main menu")
        choice = input("Select option: ")

        if choice == "1":
            sell_product(int(input("Product ID: ")), int(input("Quantity: ")))
        elif choice == "2":
            purchase_product(int(input("Product ID: ")), int(input("Quantity: ")), float(input("Cost per unit: ")))
        elif choice == "3":
            print(view_transaction_history())
        elif choice == "4":
            break

def report_menu():
    while True:
        print("\n--- Reports ---")
        print("1. Generate monthly report")
        print("2. Top selling products")
        print("3. Most expensive product")
        print("4. Average product price")
        print("5. Back to main menu")
        choice = input("Select option: ")

        if choice == "1":
            month = int(input("Month (1-12): "))
            year = int(input("Year (e.g., 2025): "))
            print(generate_monthly_report(month, year))
        elif choice == "2":
            print(get_top_selling_products(int(input("Top N products: "))))
        elif choice == "3":
            print(get_most_expensive_product())
        elif choice == "4":
            print("Average price:", average_product_price())
        elif choice == "5":
            break

def main():
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Inventory Operations")
        print("2. Stock Monitoring")
        print("3. Transactions")
        print("4. Reports")
        print("5. Exit")
        option = input("Choose an option: ")

        if option == "1":
            inventory_menu()
        elif option == "2":
            stock_menu()
        elif option == "3":
            transaction_menu()
        elif option == "4":
            report_menu()
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
