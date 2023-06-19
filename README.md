# InventoryManagmentSystem
Inventory Management Documentation
Table of Contents
Introduction
Requirements
Usage
Functions
4.1 check_stock()
4.2 update_stock()
4.3 show_stock_chart()
4.4 add_cable_window()
<a name="introduction"></a>

1. Introduction
The Inventory Management system is designed to help users manage the stock of different cables. It provides functionalities to check the stock quantity, update the stock, view a stock chart, and add new cables to the inventory. The graphical user interface (GUI) is built using the Tkinter library, and the inventory data is stored in a Python dictionary.

<a name="requirements"></a>

2. Requirements
The following are the requirements to run the Inventory Management system:

Python 3.x
Tkinter library
Matplotlib library
<a name="usage"></a>

3. Usage
To use the Inventory Management system, follow these steps:

Install the required libraries (if not already installed) by running the following command:

shell
Copy code
pip install matplotlib
Save the code in a Python file (e.g., inventory_management.py).

Import the necessary libraries by adding the following line at the beginning of your code:

python
Copy code
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
Initialize the Tkinter main window and set its properties:

python
Copy code
window = tk.Tk()
window.title("Inventory Management")
window.geometry("400x400")
window.eval('tk::PlaceWindow . center')
window.configure(background='white')
Use the provided functions and widgets to manage the inventory.

Run the application:

python
Copy code
window.mainloop()
<a name="functions"></a>

4. Functions
The Inventory Management system provides the following functions:

<a name="check_stock"></a>

4.1 check_stock()
This function retrieves the selected product from the product_combobox widget and displays its stock quantity and details in the GUI. If the product is not found in the inventory, it displays an appropriate message.

python
Copy code
def check_stock():
    product = product_combobox.get()
    if product in inventory:
        stock = inventory[product]['stock']
        unit = inventory[product]['unit']
        stock_label.config(text=f"Stock: {stock} {unit}")

        # Display product details
        details = f"Price: R{inventory[product]['price']}\n" \
                  f"Manufacturer: {inventory[product]['manufacturer']}\n" \
                  f"Description: {inventory[product]['description']}\n" \
                  f"Specifications: {inventory[product]['specifications']}"
        details_label.config(text=details)
    else:
        stock_label.config(text="Product not found")
        details_label.config(text="")
<a name="update_stock"></a>

4.2 update_stock()
This function updates the stock quantity of the selected product based on the entered quantity in the quantity_entry.
