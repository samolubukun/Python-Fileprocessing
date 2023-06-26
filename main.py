import pandas as pd

with open('SupermarketCompare.csv', 'r') as file:
    df = pd.read_csv(file, index_col=0)#index_col=0 uses the values in the first column as an index

# 1. Find the average cost of each product and the total spent in each supermarket
product_avg_cost = df.mean(axis=1)
supermarket_total_spent = df.sum(axis=0)

# Print out the results
print("Average Cost of Each Product:")
print(product_avg_cost)
print("\nTotal Spent in Each Supermarket:")
print(supermarket_total_spent)

# 2. Insert a new row into the table containing the total spend
df.loc['Total Spend'] = df.sum(axis=0) #axis=0 in pandas perform operations along the rows

# 3. Insert a new column into the table containing the average cost of each item
df['Average  Cost'] = df.mean(axis=1)  #axis=1 in pandas perform operations along the columns

# 4. Print the final table
print("\nFinal Table:")
print(df)
