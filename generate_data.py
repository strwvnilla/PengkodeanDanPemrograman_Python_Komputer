import pandas as pd

# Data penjualan
sales_data = {
    'Sale_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Date': ['2024-04-01', '2024-04-05', '2024-04-12', '2024-05-01', '2024-05-03', '2024-05-10', '2024-06-01', '2024-06-05', '2024-06-12'],
    'Product_ID': [101, 102, 103, 101, 102, 103, 101, 102, 103],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 201, 202, 203],
    'Quantity': [2, 1, 5, 1, 3, 2, 4, 2, 6],
    'Sale_Amount': [2000, 1500, 5000, 1000, 4500, 2000, 4000, 3000, 6000]
}
sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('sales.csv', index=False)

# Data pembelian
purchases_data = {
    'Purchase_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Date': ['2024-04-01', '2024-04-10', '2024-04-20', '2024-05-05', '2024-05-15', '2024-05-25', '2024-06-05', '2024-06-15', '2024-06-25'],
    'Product_ID': [101, 102, 103, 101, 102, 103, 101, 102, 103],
    'Supplier_ID': [301, 302, 303, 301, 302, 303, 301, 302, 303],
    'Quantity': [10, 5, 20, 15, 10, 25, 20, 15, 30],
    'Purchase_Amount': [8000, 7500, 20000, 12000, 15000, 25000, 16000, 22500, 30000]
}
purchases_df = pd.DataFrame(purchases_data)
purchases_df.to_csv('purchases.csv', index=False)

# Data persediaan
inventory_data = {
    'Product_ID': [101, 102, 103],
    'Stock': [29, 19, 44]
}
inventory_df = pd.DataFrame(inventory_data)
inventory_df.to_csv('inventory.csv', index=False)

# Data produk
products_data = {
    'Product_ID': [101, 102, 103],
    'Product_Name': ['Laptop X', 'Desktop Y', 'Monitor Z'],
    'Price': [1000, 1500, 1000]
}
products_df = pd.DataFrame(products_data)
products_df.to_csv('products.csv', index=False)

# Data pelanggan
customers_data = {
    'Customer_ID': [201, 202, 203, 204, 205, 206],
    'Customer_Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Michael Brown', 'Emily Davis', 'Daniel Wilson'],
    'Contact': [1234567, 2345678, 3456789, 4567890, 5678901, 6789012]
}
customers_df = pd.DataFrame(customers_data)
customers_df.to_csv('customers.csv', index=False)

# Data pemasok
suppliers_data = {
    'Supplier_ID': [301, 302, 303],
    'Supplier_Name': ['Supplier A', 'Supplier B', 'Supplier C'],
    'Contact': [1111111, 2222222, 3333333]
}
suppliers_df = pd.DataFrame(suppliers_data)
suppliers_df.to_csv('suppliers.csv', index=False)

# Data invoice
invoices_data = {
    'Invoice_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Sale_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Invoice_Date': ['2024-04-01', '2024-04-05', '2024-04-12', '2024-05-01', '2024-05-03', '2024-05-10', '2024-06-01', '2024-06-05', '2024-06-12'],
    'Total_Amount': [2000, 1500, 5000, 1000, 4500, 2000, 4000, 3000, 6000]
}
invoices_df = pd.DataFrame(invoices_data)
invoices_df.to_csv('invoices.csv', index=False)

import pandas as pd

# Membaca data dari file CSV
sales_df = pd.read_csv('sales.csv')
purchases_df = pd.read_csv('purchases.csv')
inventory_df = pd.read_csv('inventory.csv')
products_df = pd.read_csv('products.csv')
customers_df = pd.read_csv('customers.csv')
suppliers_df = pd.read_csv('suppliers.csv')
invoices_df = pd.read_csv('invoices.csv')

# Menampilkan data
print("Sales Data")
print(sales_df.head())
print("\nPurchases Data")
print(purchases_df.head())
print("\nInventory Data")
print(inventory_df.head())
print("\nProducts Data")
print(products_df.head())
print("\nCustomers Data")
print(customers_df.head())
print("\nSuppliers Data")
print(suppliers_df.head())
print("\nInvoices Data")
print(invoices_df.head())
