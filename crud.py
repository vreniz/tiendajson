import json
import os

# Path where the JSON file will be stored
DATA_FILE = os.path.join("data", "data.json")


def ensure_data_folder():
    """
    Ensures that the 'data' folder exists.
    Creates it if it does not exist.
    """
    if not os.path.exists("data"):
        os.makedirs("data")


def read_products():
    """
    Reads all products from the JSON file.

    Returns:
        list: List of product dictionaries.
    """
    if not os.path.isfile(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_products(products):
    """
    Saves the entire list of products to the JSON file.

    Args:
        products (list): List of product dictionaries.
    """
    ensure_data_folder()

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)


def create_product(product_data):
    """
    Adds a new product.

    Validates that the ID is unique.

    Returns:
        bool
    """
    products = read_products()

    for product in products:
        if product["id"] == product_data["id"]:
            print("Error: A product with this ID already exists.")
            return False

    products.append(product_data)
    save_products(products)
    return True


def update_product(id_value, id_field, new_data):
    """
    Updates a product by ID.

    Returns:
        bool
    """
    products = read_products()
    updated = False

    for product in products:
        if product[id_field] == id_value:
            product.update(new_data)
            updated = True

    if updated:
        save_products(products)

    return updated


def delete_product(id_value, id_field):
    """
    Deletes a product by ID.

    Returns:
        bool
    """
    products = read_products()
    new_products = [p for p in products if p[id_field] != id_value]

    if len(new_products) != len(products):
        save_products(new_products)
        return True

    return False


def find_product_by_id(id_value, id_field="id"):
    """
    Finds a product by ID.

    Returns:
        dict | None
    """
    products = read_products()

    for product in products:
        if product[id_field] == id_value:
            return product

    return None


def find_product_by_name(name):
    """
    Finds products by name (case insensitive).

    Returns:
        list
    """
    products = read_products()
    results = []

    for product in products:
        if product["name"].lower() == name.lower():
            results.append(product)

    return results


def delete_product_by_name(name):
    """
    Deletes products by name.

    Returns:
        bool
    """
    products = read_products()
    new_products = [p for p in products if p["name"].lower() != name.lower()]

    if len(new_products) != len(products):
        save_products(new_products)
        return True

    return False


def alert_low_stock():
    """
    Displays products with low stock.
    """
    products = read_products()
    low_stock = [p for p in products if int(p["quantity"]) < 5]

    if not low_stock:
        print("✅ No products with low stock.")
        return

    print("\n⚠️ LOW STOCK PRODUCTS:")
    for p in low_stock:
        if int(p["quantity"]) <= 2:
            print(f"🔴 CRITICAL: ID: {p['id']} | {p['name']} | Stock: {p['quantity']}")
        else:
            print(f"🟡 LOW: ID: {p['id']} | {p['name']} | Stock: {p['quantity']}")
