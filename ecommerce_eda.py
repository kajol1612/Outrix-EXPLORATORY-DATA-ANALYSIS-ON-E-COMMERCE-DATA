
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate e-commerce transaction data
np.random.seed(42)
num_records = 1000

data = {
    "InvoiceNo": np.random.choice([f'INV{1000+i}' for i in range(200)], num_records),
    "StockCode": np.random.choice([f'P{i}' for i in range(50)], num_records),
    "Description": np.random.choice(["T-Shirt", "Mug", "Notebook", "Pen", "Bag", "Shoes", "Socks"], num_records),
    "Quantity": np.random.randint(1, 10, num_records),
    "InvoiceDate": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 180, num_records), unit='d'),
    "UnitPrice": np.round(np.random.uniform(5, 50, num_records), 2),
    "CustomerID": np.random.choice([f'C{i}' for i in range(100)], num_records),
    "Country": np.random.choice(["United Kingdom", "Germany", "France", "Spain", "Italy"], num_records)
}

df = pd.DataFrame(data)
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Clean the dataset
df_cleaned = df.drop_duplicates()

# Set style
sns.set(style="whitegrid")

# Top 5 most sold products by quantity
top_products = df_cleaned.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(5)

# Top 5 products by revenue
top_revenue_products = df_cleaned.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(5)

# Top 5 customers by spending
top_customers = df_cleaned.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(5)

# Sales by country
country_sales = df_cleaned.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
top_products.plot(kind='bar', color='skyblue')
plt.title("Top 5 Products by Quantity Sold")
plt.ylabel("Total Quantity")

plt.subplot(2, 2, 2)
top_revenue_products.plot(kind='bar', color='salmon')
plt.title("Top 5 Products by Revenue")
plt.ylabel("Revenue")

plt.subplot(2, 2, 3)
top_customers.plot(kind='bar', color='limegreen')
plt.title("Top 5 Customers by Spending")
plt.ylabel("Total Spent")

plt.subplot(2, 2, 4)
country_sales.plot(kind='bar', color='gold')
plt.title("Sales by Country")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()
