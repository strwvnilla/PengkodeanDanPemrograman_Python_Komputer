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

# Menggabungkan data untuk analisis
sales_merged_df = pd.merge(sales_df, products_df, on='Product_ID')
sales_merged_df = pd.merge(sales_merged_df, customers_df, on='Customer_ID')

purchases_merged_df = pd.merge(purchases_df, products_df, on='Product_ID')
purchases_merged_df = pd.merge(purchases_merged_df, suppliers_df, on='Supplier_ID')

# Analisis statistik deskriptif
def descriptive_statistics(df, title):
    desc = df.describe()
    print(f"{title} Descriptive Statistics:")
    print(desc)
    print("\n")
    return desc

sales_desc = descriptive_statistics(sales_df, "Sales")
purchases_desc = descriptive_statistics(purchases_df, "Purchases")
inventory_desc = descriptive_statistics(inventory_df, "Inventory")
products_desc = descriptive_statistics(products_df, "Products")

# Visualisasi distribusi data
def plot_distribution(df, column, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {title}')
    plt.xlabel(title)
    plt.ylabel('Frequency')
    plt.savefig(f'distribution_{column}.png')
    plt.show()

plot_distribution(sales_df, 'Sale_Amount', 'Sale Amount')
plot_distribution(purchases_df, 'Purchase_Amount', 'Purchase Amount')
plot_distribution(inventory_df, 'Stock', 'Stock')
plot_distribution(products_df, 'Price', 'Price')

# Analisis korelasi
combined_df = pd.DataFrame({
    'Sale_Amount': sales_df['Sale_Amount'],
    'Purchase_Amount': purchases_df['Purchase_Amount'],
    'Stock': inventory_df['Stock'],
    'Price': products_df['Price']
})
correlation_matrix = combined_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()

# Menyimpan hasil analisis ke dalam file teks
with open('statistical_analysis_report.txt', 'w') as report_file:
    report_file.write("Statistical Analysis Report\n")
    report_file.write("============================\n\n")
    report_file.write("Descriptive Statistics:\n\n")
    
    report_file.write("Sales Data:\n")
    report_file.write(sales_desc.to_string())
    report_file.write("\n\n")
    
    report_file.write("Purchases Data:\n")
    report_file.write(purchases_desc.to_string())
    report_file.write("\n\n")
    
    report_file.write("Inventory Data:\n")
    report_file.write(inventory_desc.to_string())
    report_file.write("\n\n")
    
    report_file.write("Products Data:\n")
    report_file.write(products_desc.to_string())
    report_file.write("\n\n")
    
    report_file.write("Correlation Matrix:\n")
    report_file.write(correlation_matrix.to_string())
    report_file.write("\n\n")

    report_file.write("Interpretation:\n")
    for column in correlation_matrix.columns:
        report_file.write(f"Correlation with {column}:\n")
        for index in correlation_matrix.index:
            if column != index:
                corr_value = correlation_matrix.loc[index, column]
                report_file.write(f" - {index}: {corr_value:.2f} ")
                if corr_value > 0.7:
                    report_file.write("(Very Strong Correlation)\n")
                elif corr_value > 0.5:
                    report_file.write("(Strong Correlation)\n")
                elif corr_value > 0.3:
                    report_file.write("(Moderate Correlation)\n")
                elif corr_value > 0.1:
                    report_file.write("(Weak Correlation)\n")
                else:
                    report_file.write("(No or Very Weak Correlation)\n")
        report_file.write("\n")

print("Statistical analysis completed. Report saved as 'statistical_analysis_report.txt'.")
