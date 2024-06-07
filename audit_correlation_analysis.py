import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data dari file CSV
sales_df = pd.read_csv('sales.csv')
purchases_df = pd.read_csv('purchases.csv')
inventory_df = pd.read_csv('inventory.csv')
products_df = pd.read_csv('products.csv')
customers_df = pd.read_csv('customers.csv')
suppliers_df = pd.read_csv('suppliers.csv')
invoices_df = pd.read_csv('invoices.csv')

# Menggabungkan data untuk analisis korelasi
sales_merged_df = pd.merge(sales_df, products_df, on='Product_ID')
sales_merged_df = pd.merge(sales_merged_df, customers_df, on='Customer_ID')

purchases_merged_df = pd.merge(purchases_df, products_df, on='Product_ID')
purchases_merged_df = pd.merge(purchases_merged_df, suppliers_df, on='Supplier_ID')

# Membuat DataFrame gabungan untuk korelasi
combined_df = pd.DataFrame({
    'Sale_Amount': sales_df['Sale_Amount'],
    'Purchase_Amount': purchases_df['Purchase_Amount'],
    'Stock': inventory_df['Stock'],
    'Price': products_df['Price']
})

# Menghitung matriks korelasi
correlation_matrix = combined_df.corr()

# Visualisasi matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriks Korelasi')
plt.savefig('correlation_matrix.png')
plt.show()

# Menyimpan hasil korelasi ke dalam file teks
with open('correlation_analysis_report.txt', 'w') as report_file:
    report_file.write("Analisis Korelasi\n")
    report_file.write("==================\n\n")
    report_file.write("Deskripsi:\n")
    report_file.write("Analisis ini dilakukan untuk memahami hubungan antara jumlah penjualan, jumlah pembelian, persediaan, dan harga produk.\n\n")
    report_file.write("Matriks Korelasi:\n")
    report_file.write(correlation_matrix.to_string())
    report_file.write("\n\nInterpretasi:\n")

    for column in correlation_matrix.columns:
        report_file.write(f"Korelasi dengan {column}:\n")
        for index in correlation_matrix.index:
            if column != index:
                corr_value = correlation_matrix.loc[index, column]
                report_file.write(f" - {index}: {corr_value:.2f} ")
                if corr_value > 0.7:
                    report_file.write("(Korelasi sangat kuat)\n")
                elif corr_value > 0.5:
                    report_file.write("(Korelasi kuat)\n")
                elif corr_value > 0.3:
                    report_file.write("(Korelasi sedang)\n")
                elif corr_value > 0.1:
                    report_file.write("(Korelasi lemah)\n")
                else:
                    report_file.write("(Tidak ada korelasi atau korelasi sangat lemah)\n")
        report_file.write("\n")

# Menampilkan matriks korelasi
print("Matriks Korelasi:")
print(correlation_matrix)
