# Store Inventory Management System (JSON)

This project is a command-line application that allows users to manage store inventory using CRUD operations (Create, Read, Update, Delete). Data is stored persistently in a JSON file.

---

## Features

- Add new products (unique ID validation)
- View all products
- Update product information
- Delete products (by ID or name)
- Search products (by ID or name)
- Low stock alert system

---

## Project Structure

- `main_json.py` → User interface
- `crud_json.py` → Data logic and JSON handling
- `data/data.json` → Data storage

---

## Requirements

- Python 3.x

---

## How to Run

```bash
python main.py
```
## Data Structure

Each product is stored as:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 1200.5,
  "category": "Electronics",
  "quantity": 10
}
```
## Key Concepts

### JSON Storage
Data is stored as a list of dictionaries in a JSON file.

### CRUD Operations
- Create → Add product
- Read → Load all products
- Update → Modify product
- Delete → Remove product

### Validation
- Prevents duplicate IDs
- Validates numeric inputs

---

## Notes
- JSON supports complex data structures
- File is created automatically if not found
- Data is human-readable

---

## Possible Improvements
- Partial search
- GUI or web interface
- Database integration
- Error handling for corrupted JSON

---

## Author
Practice project for learning CRUD operations and JSON persistence in Python.