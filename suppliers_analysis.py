import pandas as pd

# Membaca data supplier dari file CSV
suppliers_df = pd.read_csv('suppliers.csv')
purchases_df = pd.read_csv('purchases.csv')

# 1. Supplier utama perusahaan
top_suppliers = purchases_df.groupby('Supplier_ID')['Purchase_Amount'].sum().nlargest(5)
print("Supplier Utama Perusahaan:")
print(top_suppliers)

