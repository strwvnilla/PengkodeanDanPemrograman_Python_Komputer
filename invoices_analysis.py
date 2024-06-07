import pandas as pd

# Membaca data faktur dari file CSV
invoices_df = pd.read_csv('invoices.csv')
sales_df = pd.read_csv('sales.csv')

# 1. Total pendapatan dari penjualan per periode waktu tertentu
total_revenue = sales_df['Sale_Amount'].sum()
print("Total Pendapatan dari Penjualan:", total_revenue)