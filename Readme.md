# Restaurant Billing System 

## Project Title
Restaurant Billing System (Python + JSON)

## Overview of the Project
This project is a simple console-based Restaurant Billing System developed using Python.
It allows restaurant owners to display menu items, take customer orders, generate final bills with tax, and automatically store order history for future reference.

The system is beginner-friendly and demonstrates file handling concepts using JSON (for menu storage) and text logs (for saving transactions).

## Features
- Automatically loads or creates a menu file
- Display menu with item IDs, names, and prices
- Start a new customer order
- Add items to the order with chosen quantity
- Calculate subtotal, tax (5%), and total bill
- Generate a formatted final bill
- Save every transaction to a log file with timestamp
- Simple console-based interface

## Technologies / Tools Used
- Python 3
- JSON file handling
- Text file logging
- Built-in Python libraries (json, datetime)

## Steps to Install & Run the Project
### 1. Download the Files
Ensure the folder contains:
```
restaurant.py
menu_simple.json   
order_log_simple.txt   
```

### 2. No Dependencies Required
This project uses only Python’s built-in modules.

### 3. Run the Program
```
python restaurant.py
```

### 4. File Initialization
- menu_simple.json → Stores menu items 
- order_log_simple.txt → Stores order records 

## Instructions for Testing
1. Launch the program
2. Choose "Show Menu" to view available items
3. Start a new order
4. Add items using their item ID
5. Finalize bill to see subtotal, tax, and grand total
6. Check order_log_simple.txt to confirm the transaction was logged