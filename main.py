from crud import *
import re


def show_menu():
    print("\n--- STORE INVENTORY (JSON) ---")
    print("1. Create product")
    print("2. Read products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Search product")
    print("6. Exit")
    print("7. Low stock alert")


def read_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Must be positive.")
            else:
                return value
        except ValueError:
            print("Invalid number.")


def read_float(message):
    pattern = r"^\d+([.,]\d+)?$"

    while True:
        value = input(message).strip()

        if not value:
            print("Cannot be empty.")
            continue

        if not re.match(pattern, value):
            print("Invalid format.")
            continue

        value = float(value.replace(",", "."))

        if value <= 0:
            print("Must be greater than 0.")
        else:
            return value


def read_text(message):
    while True:
        text = input(message).strip()

        if not text:
            print("Cannot be empty.")
            continue

        if text.isdigit():
            print("Cannot be only numbers.")
            continue

        return text


def get_product_data():
    return {
        "id": read_positive_int("ID: "),
        "name": read_text("Name: "),
        "price": read_float("Price: "),
        "category": read_text("Category: "),
        "quantity": read_positive_int("Stock: "),
    }


def get_update_data():
    return {
        "name": read_text("Name: "),
        "price": read_float("Price: "),
        "category": read_text("Category: "),
        "quantity": read_positive_int("Stock: "),
    }


if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Choose option: ")

        if option == "1":
            if create_product(get_product_data()):
                print("Saved.")

        elif option == "2":
            print(read_products())

        elif option == "3":
            id_value = int(input("ID: "))
            print(
                "Updated."
                if update_product(id_value, "id", get_update_data())
                else "Not found."
            )

        elif option == "4":
            mode = input("(1) ID (2) Name: ")

            if mode == "1":
                print(
                    "Deleted."
                    if delete_product(int(input("ID: ")), "id")
                    else "Not found."
                )
            else:
                print(
                    "Deleted."
                    if delete_product_by_name(input("Name: "))
                    else "Not found."
                )

        elif option == "5":
            mode = input("(1) ID (2) Name: ")

            if mode == "1":
                print(find_product_by_id(int(input("ID: "))) or "Not found.")
            else:
                print(find_product_by_name(input("Name: ")) or "No results.")

        elif option == "6":
            break

        elif option == "7":
            alert_low_stock()
