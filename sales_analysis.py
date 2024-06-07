import pandas as pd
import matplotlib.pyplot as plt

# Membaca data penjualan dari file CSV
sales_df = pd.read_csv('sales.csv')

# 1. Total penjualan per periode waktu tertentu
total_sales = sales_df['Sale_Amount'].sum()
print("Total Penjualan:", total_sales)

# 2. Tren penjualan dari waktu ke waktu
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df.set_index('Date', inplace=True)
monthly_sales = sales_df.resample('M').sum()
monthly_sales.plot(kind='line', y='Sale_Amount', marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan')
plt.show()

# 3. Produk-produk yang paling laris terjual
top_products = sales_df.groupby('Product_ID')['Sale_Amount'].sum().nlargest(5)
print("Produk-produk yang Paling Laris Terjual:")
print(top_products)

# 4. Distribusi jumlah penjualan untuk setiap produk
product_sales_distribution = sales_df.groupby('Product_ID')['Sale_Amount'].sum()
product_sales_distribution.plot(kind='bar')
plt.title('Distribusi Jumlah Penjualan untuk Setiap Produk')
plt.xlabel('Product ID')
plt.ylabel('Total Penjualan')
plt.show()
