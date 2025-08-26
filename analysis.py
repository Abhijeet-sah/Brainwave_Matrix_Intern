import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/sales_data.csv')

# Category Contribution
category_sales = df.groupby('Category')['Price'].sum()
category_sales.plot(kind='pie', autopct='%1.1f%%', title='Category Contribution')
plt.savefig('images/category_pie.png')
plt.close()

# Monthly Sales
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')
monthly_sales = df.groupby('Month')['Price'].sum().reindex([
    'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.savefig('images/monthly_sales.png')
plt.close()

# Payment Methods
payment_sales = df.groupby('PaymentMethod')['Price'].sum()
payment_sales.plot(kind='bar', title='Payment Method Distribution')
plt.ylabel("Revenue")
plt.savefig('images/payment_bar.png')
plt.close()

print("Analysis complete. Charts saved in images/ folder.")
