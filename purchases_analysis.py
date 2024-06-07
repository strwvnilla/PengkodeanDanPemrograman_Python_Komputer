import pandas as pd
import matplotlib.pyplot as plt

# Membaca data pembelian dari file CSV
purchases_df = pd.read_csv('purchases.csv')

# 1. Total pengeluaran untuk pembelian produk
total_purchases = purchases_df['Purchase_Amount'].sum()
print("Total Pengeluaran untuk Pembelian:", total_purchases)

# 2. Tren pembelian dari waktu ke waktu
purchases_df['Date'] = pd.to_datetime(purchases_df['Date'])
purchases_df.set_index('Date', inplace=True)
monthly_purchases = purchases_df.resample('M').sum()
monthly_purchases.plot(kind='line', y='Purchase_Amount', marker='o')
plt.title('Tren Pembelian Bulanan')
plt.xlabel('Tanggal')
plt.ylabel('Total Pembelian')
plt.show()

# 3. Supplier utama perusahaan
top_suppliers = purchases_df.groupby('Supplier_ID')['Purchase_Amount'].sum().nlargest(5)
print("Supplier Utama Perusahaan:")
print(top_suppliers)

# 4. Distribusi jumlah pembelian untuk setiap produk
product_purchases_distribution = purchases_df.groupby('Product_ID')['Purchase_Amount'].sum()
product_purchases_distribution.plot(kind='bar')
plt.title('Distribusi Jumlah Pembelian untuk Setiap Produk')
plt.xlabel('Product ID')
plt.ylabel('Total Pembelian')
plt.show()
