import pandas as pd
import matplotlib.pyplot as plt

# Membaca data persediaan dari file CSV
inventory_df = pd.read_csv('inventory.csv')

# 1. Stok rata-rata untuk setiap produk
average_stock = inventory_df.groupby('Product_ID')['Stock'].mean()
print("Stok Rata-rata untuk Setiap Produk:")
print(average_stock)

# 2. Tren stok dari waktu ke waktu
inventory_df['Date'] = pd.to_datetime(inventory_df['Date'])
inventory_df.set_index('Date', inplace=True)
monthly_stock = inventory_df.resample('M').mean()
monthly_stock.plot(kind='line', y='Stock', marker='o')
plt.title('Tren Stok Bulanan')
plt.xlabel('Tanggal')
plt.ylabel('Stok Rata-rata')
plt.show()

# 3. Stok berubah dari waktu ke waktu
stock_changes = inventory_df['Stock'].diff()
print("Perubahan Stok dari Waktu ke Waktu:")
print(stock_changes)

# 4. Distribusi stok untuk setiap produk
product_stock_distribution = inventory_df.groupby('Product_ID')['Stock'].mean()
product_stock_distribution.plot(kind='bar')
plt.title('Distribusi Stok untuk Setiap Produk')
plt.xlabel('Product ID')
plt.ylabel('Stok Rata-rata')
plt.show()
