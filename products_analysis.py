import pandas as pd
import matplotlib.pyplot as plt

# Membaca data produk dari file CSV
products_df = pd.read_csv('products.csv')

# 1. Harga rata-rata untuk setiap produk
average_price = products_df.groupby('Product_ID')['Price'].mean()
print("Harga Rata-rata untuk Setiap Produk:")
print(average_price)

# 2. Tren harga dari waktu ke waktu
# Misalkan kolom 'Date' adalah tanggal perubahan harga
# Jika ada kolom tanggal perubahan harga, gunakan kolom tersebut
# Jika tidak, Anda mungkin perlu data tambahan atau asumsi lain
# Contoh:
# products_df['Date'] = pd.to_datetime(products_df['Date'])
# products_df.set_index('Date', inplace=True)
# monthly_price = products_df.resample('M').mean()
# monthly_price.plot(kind='line', y='Price', marker='o')
# plt.title('Tren Harga Bulanan')
# plt.xlabel('Tanggal')
# plt.ylabel('Harga Rata-rata')
# plt.show()

# 3. Produk dengan harga jual tertinggi atau terendah
highest_price_product = products_df.loc[products_df['Price'].idxmax()]
lowest_price_product = products_df.loc[products_df['Price'].idxmin()]
print("Produk dengan Harga Jual Tertinggi:")
print(highest_price_product)
print("Produk dengan Harga Jual Terendah:")
print(lowest_price_product)

# 4. Distribusi harga untuk setiap produk
product_price_distribution = products_df.groupby('Product_ID')['Price'].mean()
product_price_distribution.plot(kind='bar')
plt.title('Distribusi Harga untuk Setiap Produk')
plt.xlabel('Product ID')
plt.ylabel('Harga Rata-rata')
plt.show()
