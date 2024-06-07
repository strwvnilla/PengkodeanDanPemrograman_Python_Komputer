import pandas as pd
import matplotlib.pyplot as plt

# Membaca data pelanggan dari file CSV
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')

# 1. Pelanggan terbesar dari perusahaan
top_customers = sales_df.groupby('Customer_ID')['Sale_Amount'].sum().nlargest(5)
print("Pelanggan Terbesar dari Perusahaan:")
print(top_customers)

# 2. Tren dalam perilaku pembelian pelanggan dari waktu ke waktu
# Misalkan kolom 'Date' adalah tanggal pembelian
# Jika ada kolom tanggal pembelian, gunakan kolom tersebut
# Jika tidak, Anda mungkin perlu data tambahan atau asumsi lain
# Contoh:
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df.set_index('Date', inplace=True)
monthly_sales = sales_df.resample('M').sum()
monthly_sales.plot(kind='line', y='Sale_Amount', marker='o')
plt.title('Tren Pembelian Bulanan Pelanggan')
plt.xlabel('Tanggal')
plt.ylabel('Total Pembelian')
plt.show()

# 3. Distribusi jumlah pembelian untuk setiap pelanggan
customer_sales_distribution = sales_df.groupby('Customer_ID')['Sale_Amount'].sum()
customer_sales_distribution.plot(kind='bar')
plt.title('Distribusi Jumlah Pembelian untuk Setiap Pelanggan')
plt.xlabel('Customer ID')
plt.ylabel('Total Penjualan')
plt.show()
