import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# ------------------------------
# Step 1: Load the Data
# ------------------------------
# Load datasets
orders = pd.read_csv("C:/Users/hp/Downloads/archive (1)/blinkit_orders.csv")
order_items = pd.read_csv("C:/Users/hp/Downloads/archive (1)/blinkit_order_items.csv")
products = pd.read_csv("C:/Users/hp/Downloads/archive (1)/blinkit_products.csv")

# Display basic info
print(orders.info())
print(order_items.info())
print(products.info())


# Step 2: Standardize Column Names
# ------------------------------
orders.columns = orders.columns.str.strip()
order_items.columns = order_items.columns.str.strip()
products.columns = products.columns.str.strip()
print("Step 2: Column names standardized.")

# ------------------------------
# Step 3: Check for Duplicates
# ------------------------------
orders.drop_duplicates(inplace=True)
order_items.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
print("Step 3: Duplicates removed.")

# ------------------------------
# Step 4: Convert Date Columns
# ------------------------------
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
print("Step 4: order_date column converted to datetime.")

# ------------------------------
# Step 5: Drop Nulls in Essential Fields
# ------------------------------
orders.dropna(subset=['order_id', 'order_date'], inplace=True)
order_items.dropna(subset=['order_id', 'product_id', 'quantity', 'unit_price'], inplace=True)
products.dropna(subset=['product_id', 'product_name', 'category'], inplace=True)
print(" Step 5: Null values in essential fields dropped.")

# ------------------------------
# Step 6: Validate and Fix Data Types
# ------------------------------
order_items['quantity'] = pd.to_numeric(order_items['quantity'], errors='coerce')
order_items['unit_price'] = pd.to_numeric(order_items['unit_price'], errors='coerce')

# Drop rows with non-positive values
initial_rows = order_items.shape[0]
order_items = order_items[(order_items['quantity'] > 0) & (order_items['unit_price'] > 0)]
removed_rows = initial_rows - order_items.shape[0]
print(f" Step 6: Cleaned invalid quantity/price. Removed {removed_rows} rows.")

# ------------------------------
# Step 7: Clean Text Fields
# ------------------------------
products['product_name'] = products['product_name'].str.strip().str.title()
products['category'] = products['category'].str.strip().str.title()
print(" Step 7: Text fields cleaned and standardized.")

# ------------------------------
# Final Shape Check
# ------------------------------
print("Final Data Shapes:")

#________________________________________________________________________________________________________________________
# ------------------------------
# Step 8: Merge Orders and Order Items
# ------------------------------
order_data = pd.merge(order_items, orders, on='order_id', how='left')
print(f"Step 8: Merged orders and order_items. Shape: {order_data.shape}")

# ------------------------------
# Step 9: Merge with Product Information
# ------------------------------
sales_data = pd.merge(order_data, products, on='product_id', how='left')
print(f"Step 9: Merged with products data. Shape: {sales_data.shape}")

# ------------------------------
# Step 10: Create Revenue Column
# ------------------------------
sales_data['revenue'] = sales_data['quantity'] * sales_data['price']
print("Step 10: Revenue column created.")

# ------------------------------
# Step 11: Drop Rows with Missing Product Info (if any)
# ------------------------------
initial_shape = sales_data.shape
sales_data.dropna(subset=['product_name', 'category'], inplace=True)
final_shape = sales_data.shape
print(f"Step 11: Dropped rows with missing product info. Rows removed: {initial_shape[0] - final_shape[0]}")

# ------------------------------
# Step 12: Final Dataset Overview
# ------------------------------
print(" Final sales_data columns:", sales_data.columns.tolist())
print(" Final sales_data shape:", sales_data.shape)
print(" Sample records:")
print(sales_data.head())
print(" Data merging complete and ready for analysis.")





#Top 10 Products by Revenue
top_products_revenue = sales_data.groupby('product_name')['revenue'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products_revenue.values, y=top_products_revenue.index, palette='viridis')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

print("Top 10 products by revenue:")
print(top_products_revenue)

#Top 10 Products by Quantity Sold
top_products_quantity = sales_data.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products_quantity.values, y=top_products_quantity.index, palette='magma')
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

print("Top 10 products by quantity sold:")
print(top_products_quantity)



# Revenue by Category
category_revenue = sales_data.groupby('category')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=category_revenue.values, y=category_revenue.index, palette='coolwarm')
plt.title(" Revenue by Product Category")
plt.xlabel("Revenue")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

print("Revenue by category:")
print(category_revenue)


#Monthly Sales Trend
# Extract month and year from order_date
sales_data['order_month'] = sales_data['order_date'].dt.to_period('M')

monthly_revenue = sales_data.groupby('order_month')['revenue'].sum()

plt.figure(figsize=(14, 6))
monthly_revenue.plot(marker='o', color='teal')
plt.title(" Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Monthly revenue trend:")
print(monthly_revenue)

#Save Clean Dataset (Optional)
sales_data.to_csv("blinkit_sales_cleaned.csv", index=False)
print(" Cleaned dataset saved as 'blinkit_sales_cleaned.csv'")





