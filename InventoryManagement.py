import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt

# inventory data
inventory = {
    'HDMI Cable': {
        'stock': 20,
        'unit': 'm',
        'price': 99.99,
        'manufacturer': 'ABC Electronics',
        'description': 'High-quality HDMI cable for audio and video transmission.',
        'specifications': 'Length: 2 meters, Connector: HDMI male to male'
    },
    'Ethernet Cable': {
        'stock': 15,
        'unit': 'm',
        'price': 49.99,
        'manufacturer': 'XYZ Cables',
        'description': 'Ethernet cable for high-speed internet connectivity.',
        'specifications': 'Length: 3 meters, Connector: RJ45'
    },
    'USB Cable': {
        'stock': 30,
        'unit': 'm',
        'price': 29.99,
        'manufacturer': 'PQR Tech',
        'description': 'USB cable for data transfer and charging.',
        'specifications': 'Length: 1 meter, Connector: USB-A to USB-B'
    },
    'Power Cable': {
        'stock': 25,
        'unit': 'm',
        'price': 79.99,
        'manufacturer': 'PowerTech',
        'description': 'Power cable for electrical devices.',
        'specifications': 'Length: 2 meters, Connector: Standard power plug'
    },
    'VGA Cable': {
        'stock': 18,
        'unit': 'm',
        'price': 59.99,
        'manufacturer': 'VGA Solutions',
        'description': 'VGA cable for video transmission.',
        'specifications': 'Length: 1.5 meters, Connector: VGA male to male'
    },
    'DisplayPort Cable': {
        'stock': 12,
        'unit': 'm',
        'price': 69.99,
        'manufacturer': 'DisplayTech',
        'description': 'DisplayPort cable for high-resolution video and audio.',
        'specifications': 'Length: 2 meters, Connector: DisplayPort male to male'
    },
    'Audio Cable': {
        'stock': 40,
        'unit': 'm',
        'price': 39.99,
        'manufacturer': 'AudioTech',
        'description': 'Audio cable for high-quality sound transmission.',
        'specifications': 'Length: 1 meter, Connector: 3.5mm stereo jack'
    },
    'Coaxial Cable': {
        'stock': 35,
        'unit': 'm',
        'price': 89.99,
        'manufacturer': 'Coaxial Solutions',
        'description': 'Coaxial cable for TV and antenna connections.',
        'specifications': 'Length: 1.5 meters, Connector: Coaxial male to male'
    },
    'Fiber Optic Cable': {
        'stock': 10,
        'unit': 'm',
        'price': 129.99,
        'manufacturer': 'FiberTech',
        'description': 'Fiber optic cable for high-speed data transmission.',
        'specifications': 'Length: 2 meters, Connector: Fiber optic connectors'
    },
    'Serial Cable': {
        'stock': 5,
        'unit': 'm',
        'price': 19.99,
        'manufacturer': 'SerialTech',
        'description': 'Serial cable for connecting devices using serial communication.',
        'specifications': 'Length: 1 meter, Connector: DB9 male to female'
    },
    'Parallel Cable': {
        'stock': 8,
        'unit': 'm',
        'price': 24.99,
        'manufacturer': 'Parallel Solutions',
        'description': 'Parallel cable for connecting devices using parallel communication.',
        'specifications': 'Length: 1 meter, Connector: DB25 male to male'
    },
    'DVI Cable': {
        'stock': 30,
        'unit': 'm',
        'price': 59.99,
        'manufacturer': 'DVI Tech',
        'description': 'DVI cable for digital video transmission.',
        'specifications': 'Length: 1.5 meters, Connector: DVI male to male'
    },
    'Thunderbolt Cable': {
        'stock': 12,
        'unit': 'm',
        'price': 149.99,
        'manufacturer': 'ThunderTech',
        'description': 'Thunderbolt cable for high-speed data and video transmission.',
        'specifications': 'Length: 2 meters, Connector: Thunderbolt male to male'
    },
    'FireWire Cable': {
        'stock': 20,
        'unit': 'm',
        'price': 79.99,
        'manufacturer': 'FireTech',
        'description': 'FireWire cable for high-speed data transfer.',
        'specifications': 'Length: 1 meter, Connector: FireWire 800 male to male'
    },
    'SATA Cable': {
        'stock': 15,
        'unit': 'm',
        'price': 39.99,
        'manufacturer': 'SATA Solutions',
        'description': 'SATA cable for connecting storage devices.',
        'specifications': 'Length: 0.5 meters, Connector: SATA male to male'
    },
    'Network Cable': {
        'stock': 40,
        'unit': 'm',
        'price': 59.99,
        'manufacturer': 'NetTech',
        'description': 'Network cable for wired network connections.',
        'specifications': 'Length: 2 meters, Connector: RJ45'
    },
    'Patch Cable': {
        'stock': 25,
        'unit': 'm',
        'price': 49.99,
        'manufacturer': 'Patch Solutions',
        'description': 'Patch cable for connecting network devices in a rack.',
        'specifications': 'Length: 1.5 meters, Connector: RJ45'
    },
    'Modem Cable': {
        'stock': 30,
        'unit': 'm',
        'price':29.99,
        'manufacturer': 'ModemTech',
        'description': 'Modem cable for connecting a modem to a computer.',
        'specifications': 'Length: 1 meter, Connector: RJ11'
    },
    'Router Cable': {
        'stock': 18,
        'unit': 'm',
        'price': 69.99,
        'manufacturer': 'RouterTech',
        'description': 'Router cable for connecting a router to a modem.',
        'specifications': 'Length: 1.5 meters, Connector: RJ45'
    },
    'Printer Cable': {
        'stock': 12,
        'unit': 'm',
        'price': 34.99,
        'manufacturer': 'PrinterTech',
        'description': 'Printer cable for connecting a printer to a computer.',
        'specifications': 'Length: 1 meter, Connector: USB-A to USB-B'
    }
}



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

def update_stock():
    product = product_combobox.get()
    quantity = int(quantity_entry.get())

    if product in inventory:
        inventory[product]['stock'] += quantity
    else:
        inventory[product] = {'stock': quantity, 'unit': 'm'}

    messagebox.showinfo("Success", "Stock updated successfully!")
    product_combobox.set('')
    quantity_entry.delete(0, tk.END)

def show_stock_chart():
    products = list(inventory.keys())
    stock_levels = [inventory[product]['stock'] for product in products]

    plt.bar(products, stock_levels)
    plt.xlabel('Product')
    plt.ylabel('Stock Level')
    plt.xticks(rotation=90)
    plt.title('Inventory Stock Levels')
    plt.tight_layout()
    plt.show()

# Create the main window
window = tk.Tk()
window.title("Inventory Management")

# Set the window size and center it on the screen
window.geometry("400x400")
window.eval('tk::PlaceWindow . center')

# Set the background color
window.configure(background='white')




# Customize colors
product_label = tk.Label(window, text="Product:", foreground='black')
product_label.pack()

product_combobox = ttk.Combobox(window, values=list(inventory.keys()))
product_combobox.pack()

stock_button = tk.Button(window, text="Check Stock", command=check_stock, background='lightblue', foreground='black')
stock_button.pack()

stock_label = tk.Label(window, text="", background='white')
stock_label.pack()

quantity_label = tk.Label(window, text="Quantity (in meters):", foreground='black')
quantity_label.pack()

quantity_entry = tk.Entry(window)
quantity_entry.pack()

update_button = tk.Button(window, text="Update Stock", command=update_stock, background='lightgreen', foreground='black')
update_button.pack()

chart_button = tk.Button(window, text="Show Stock Chart", command=show_stock_chart, background='lightyellow', foreground='black')
chart_button.pack()

details_label = tk.Label(window, text="", background='white')
details_label.pack()

def add_cable_window():
    # Create a new window
    cable_window = tk.Toplevel(window)
    cable_window.title("Add Cable")

    # Create and position the labels and entry widgets for additional information
    stock_label = tk.Label(cable_window, text="Stock:")
    stock_label.pack()

    stock_entry = tk.Entry(cable_window)
    stock_entry.pack()

    price_label = tk.Label(cable_window, text="Price:")
    price_label.pack()

    price_entry = tk.Entry(cable_window)
    price_entry.pack()

    manufacturer_label = tk.Label(cable_window, text="Manufacturer:")
    manufacturer_label.pack()

    manufacturer_entry = tk.Entry(cable_window)
    manufacturer_entry.pack()

    description_label = tk.Label(cable_window, text="Description:")
    description_label.pack()

    description_entry = tk.Entry(cable_window)
    description_entry.pack()

    specifications_label = tk.Label(cable_window, text="Specifications:")
    specifications_label.pack()

    specifications_entry = tk.Entry(cable_window)
    specifications_entry.pack()

    # Create a function to handle adding the cable with the entered information
    def add_cable():
        cable_name = cable_name_entry.get()
        stock = int(stock_entry.get())
        price = price_entry.get()
        manufacturer = manufacturer_entry.get()
        description = description_entry.get()
        specifications = specifications_entry.get()

        if cable_name and stock and price and manufacturer and description and specifications:
            if cable_name in inventory:
                messagebox.showinfo("Error", "Cable already exists.")
            else:
                inventory[cable_name] = {
                    'stock': stock,
                    'unit': 'm',
                    'price': price,
                    'manufacturer': manufacturer,
                    'description': description,
                    'specifications': specifications
                }
                product_combobox['values'] = list(inventory.keys())
                messagebox.showinfo("Success", "Cable added successfully!")
                cable_window.destroy()
        else:
            messagebox.showinfo("Error", "Please enter all cable details.")

    # Create the "Add Cable" button in the new window
    add_button = tk.Button(cable_window, text="Add Cable", command=add_cable)
    add_button.pack()

cable_name_label = tk.Label(window, text="Cable Name:")
cable_name_label.pack()

cable_name_entry = tk.Entry(window)
cable_name_entry.pack()

add_cable_button = tk.Button(window, text="Add Cable", command=add_cable_window)
add_cable_button.pack()


# Run the application
window.mainloop()
