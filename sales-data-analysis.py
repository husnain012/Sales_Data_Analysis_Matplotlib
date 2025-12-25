import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*50)
print("SALES DATA ANALYSIS")
print("="*50)
print("\n")

# Load and explore data
data = pd.read_csv("sales_data.csv")
print("--------------- Overview ---------------")
print("\n")
print(data.head())
print("\n")
print(data.info())
print("\n")

# Total sales by product category
total_sales_category = data.groupby("product_category")["sales_amount"].sum()
print("--------------- Total sales by product category ---------------")
print("\n")
print(total_sales_category)
print("\n")

# Monthly sales trend
data['purchase_date'] = pd.to_datetime(data['purchase_date'])
data["Month"] = data["purchase_date"].dt.month_name()
monthly_sales = data.groupby("Month")["sales_amount"].sum()
print("--------------- Monthly sales trend ---------------")
print("\n")
print(monthly_sales)
print("\n")

# Top 5 Most Profitable Products
top_profitable = data.sort_values(by="profit", ascending=False)
print("--------------- Top 5 Most Profitable Products ---------------")
print("\n")
print(top_profitable[['order_id', 'product_category', 'profit', 'sales_amount']].head())
print("\n")

# Customer age distribution
age_stats = data["customer_age"].describe()
print("--------------- Customer age distribution ---------------")
print("\n")
print(age_stats)
print("\n")

# Best Performing Region by Sales
region_sales = data.groupby("region")["sales_amount"].sum()
print("--------------- Best Performing Region by Sales ---------------")
print("\n")
print(region_sales)
print("\n")

# Correlation Between Sales, Profit, and Rating
correlation_matrix = data[['sales_amount', 'profit', 'rating']].corr()
print("--------------- Correlation Between Sales, Profit, and Rating ---------------")
print("\n")
print(correlation_matrix)
print("\n")

# Sales by Categories Visualization
print("--------------- Sales by Category (Visualization) ---------------")
print("\n")
plt.figure(figsize=(10, 6))
plt.bar(total_sales_category.index, total_sales_category.values, color="skyblue")
plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

# Add value labels
for i, v in enumerate(total_sales_category.values):
    plt.text(i, v + max(monthly_sales.values)*0.01, f"{v:,.0f}", ha="center")

plt.savefig("Visualization/sales_by_category.png")
plt.show()
print("\n")

# Monthly Sales Trend Visualization
print("--------------- Monthly Sales Trend Visualization ---------------")
print("\n")
plt.style.use("ggplot")
plt.figure(figsize=(12, 6))

plt.plot(monthly_sales.index, monthly_sales.values, 
         marker="o", linewidth=2.5, markersize=8, 
         color="#2E86AB", markerfacecolor="#A23B72")

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales Amount ($)", fontsize=12)

# Add value labels on points
for i, v in enumerate(monthly_sales.values):
    plt.text(i, v + max(monthly_sales.values)*0.02, f"${v:,}", ha="center")

plt.grid(True, alpha=0.3)

plt.savefig("Visualization/monthly_trends.png")
plt.show()