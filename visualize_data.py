import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
sales_df = pd.read_csv('sales.csv')
purchases_df = pd.read_csv('purchases.csv')
inventory_df = pd.read_csv('inventory.csv')
products_df = pd.read_csv('products.csv')
customers_df = pd.read_csv('customers.csv')
suppliers_df = pd.read_csv('suppliers.csv')
invoices_df = pd.read_csv('invoices.csv')

# Menggabungkan data sales dengan data produk untuk mendapatkan nama produk
sales_merged_df = pd.merge(sales_df, products_df, on='Product_ID')
purchases_merged_df = pd.merge(purchases_df, products_df, on='Product_ID')

# Visualisasi 1: Total penjualan per produk
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_Name', y='Sale_Amount', data=sales_merged_df, estimator=sum)
plt.title('Total Penjualan per Produk')
plt.xlabel('Produk')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_penjualan_per_produk.png')
plt.show()

# Visualisasi 2: Total pembelian per produk
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_Name', y='Purchase_Amount', data=purchases_merged_df, estimator=sum)
plt.title('Total Pembelian per Produk')
plt.xlabel('Produk')
plt.ylabel('Total Pembelian')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_pembelian_per_produk.png')
plt.show()

# Visualisasi 3: Persediaan per produk
plt.figure(figsize=(10, 6))
sns.barplot(x='Product_Name', y='Stock', data=pd.merge(inventory_df, products_df, on='Product_ID'))
plt.title('Persediaan per Produk')
plt.xlabel('Produk')
plt.ylabel('Persediaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('persediaan_per_produk.png')
plt.show()

# Visualisasi 4: Total penjualan per bulan
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df['Month'] = sales_df['Date'].dt.to_period('M')
monthly_sales = sales_df.groupby('Month')['Sale_Amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sale_Amount', data=monthly_sales, marker='o')
plt.title('Total Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_penjualan_per_bulan.png')
plt.show()

# Visualisasi 5: Total pembelian per bulan
purchases_df['Date'] = pd.to_datetime(purchases_df['Date'])
purchases_df['Month'] = purchases_df['Date'].dt.to_period('M')
monthly_purchases = purchases_df.groupby('Month')['Purchase_Amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Purchase_Amount', data=monthly_purchases, marker='o')
plt.title('Total Pembelian per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Pembelian')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_pembelian_per_bulan.png')
plt.show()
