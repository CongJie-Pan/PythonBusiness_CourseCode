import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from pandas.plotting import parallel_coordinates

print("===================================")

# set plt style
pd.set_option('display.max_columns', 500)

df = pd.read_csv('Groceries_dataset.csv')
df.head()

# Create TransactionID which is a combination of Member_number and Date
df['Member_number'] = df['Member_number'].astype(str)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
df['TransactionID'] = df['Member_number'].astype(str) + '-' + df['Date']

print(f"The dataset covers {df['Date'].min()} to {df['Date'].max()}")
print(f"There are unique {df['Member_number'].nunique()} customers in the dataset")
print(f"There are unique {df['itemDescription'].nunique()} items in the dataset")
print(f"There are unique {df['TransactionID'].nunique()} transactions in the dataset")
print("===================================")

#%%
# Monthly sales

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Extract the month and year
df['YearMonth'] = df['Date'].dt.to_period('M')

# Aggregate transactions by month
monthly_purchases = df.groupby('YearMonth').size()

# Plotting
plt.figure(figsize=(14,7))
monthly_purchases.plot(kind='line')
plt.title('Monthly Purchases')
plt.ylabel('Number of Transactions')
plt.xlabel('Month')
plt.grid(True)
plt.show()

#%%

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Extract the month and year
df['YearMonth'] = df['Date'].dt.to_period('M')

# Create a dataframe that aggregates the count of each item on a monthly basis
item_monthly_sales = df.groupby(['YearMonth', 'itemDescription']).size().unstack().fillna(0)

# Define the start and end months for the period of interest
start_month = pd.Period('2014-12')
end_month = pd.Period('2015-01')

# Calculate the difference in sales for each item between start and end months
growth_data = item_monthly_sales.loc[end_month] - item_monthly_sales.loc[start_month]

# Sort the items based on this difference
sorted_growth = growth_data.sort_values(ascending=False)

print('Top 10 Growing Items from Dec 2014 to Jan 2015')
# show the top 10 items
sorted_growth.head(10)
print("===================================")


#%%

# Top 10 items sold
top_items = df['itemDescription'].value_counts().nlargest(10)
print("Top 10 items sold:")
print(top_items)
print("===================================")

#%%

# Filter the dataframe to only include the top 15 items
top_items_over_time = df[df['itemDescription'].isin(top_items.index)]

# Get the colors from the tab20 colormap
colors = plt.cm.tab20.colors

# Plotting
plt.figure(figsize=(25,10))
for idx, item in enumerate(top_items.index):
    monthly_data = top_items_over_time[top_items_over_time['itemDescription'] == item].groupby('YearMonth').size()
    monthly_data.plot(label=item, color=colors[idx])

plt.legend()
plt.title('Top 10 Items Purchased Over Time')
plt.ylabel('Number of Transactions')
plt.xlabel('Month')
plt.grid(True)
plt.show()

#%%

frequent_shoppers = df.groupby('Member_number').size().nlargest(10)
# format and print
frequent_shoppers = pd.DataFrame(frequent_shoppers).reset_index()
frequent_shoppers.columns = ['Member_number', 'Number of Transactions']
frequent_shoppers

#%%

# use transactionid to show average # of items per transaction
avg_items_per_transaction = df.groupby('TransactionID')['itemDescription'].size().mean()
print(f"The average number of items per transaction is {round(avg_items_per_transaction, 2)}")
#%%

### Apriori

# Group by TransactionID and create a list of items
transactions = df.groupby('TransactionID')['itemDescription'].apply(list).reset_index(name='Items')

# Use TransactionEncoder
te = TransactionEncoder()
te_array = te.fit_transform(transactions['Items'])

# Convert to DataFrame
basket = pd.DataFrame(te_array, columns=te.columns_)

# Add TransactionID back to the DataFrame
basket['TransactionID'] = transactions['TransactionID']

basket.head()

#%%

'''
 Now we can apply the Apriori algorithm to find frequent itemsets. 
 You'll need to specify a minimum support value, which is the minimum 
 fraction of transactions in which an itemset appears.
'''

# Drop the TransactionID column before applying Apriori
basket_sets = basket.drop('TransactionID', axis=1)

# Apply the Apriori algorithm
frequent_itemsets = apriori(basket_sets, min_support=0.0075, use_colnames=True)

frequent_itemsets

# # most frequent item(set)s
# frequent_itemsets.iloc[np.argsort(frequent_itemsets['support'])[-5:], :]

# Check if there are itemsets with more than one item
multi_itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) > 1)]
print(multi_itemsets)

print("===================================")
#%%

# Generate association rules with a minimum lift of 1 (adjust as needed)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=.001)

# rules = rules[(rules['lift'] >= .01) & (rules['confidence'] >= 0.005)]

# round all values to 2 decimal places
rules = rules.round(2)
rules

# remove the parentheses from the antecedents and consequents values
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x)[0]).astype("unicode")
rules['consequents'] = rules['consequents'].apply(lambda x: list(x)[0]).astype("unicode")

rules.head()
#%%

# Visualize Rules the rules

# plt.figure(figsize=(10, 6))
# sns.scatterplot(x="support", y="confidence", size="lift", hue="lift", data=rules)
# plt.xlabel("Support")
# plt.ylabel("Confidence")
# plt.title("Support vs Confidence")
# plt.show()

# Create a pivot table for lift values
pivot = rules.pivot(index='antecedents', columns='consequents', values='lift')

# Generate heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, cmap="YlGnBu")
plt.title("Lift Heatmap")
plt.show()
#%%

# Create a new directed graph from edges
G = nx.from_pandas_edgelist(rules, source='antecedents', target='consequents', edge_attr=True, create_using=nx.DiGraph())

# Create a new matplotlib axes object
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the graph on the axes object
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, ax=ax)
labels = nx.get_edge_attributes(G, 'lift')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
ax.set_title("Itemset Network")

# Show the plot
plt.show()

#%%

# Getting the most popular association rules?

# top_patterns?

# test to see which items to recommend, after seeing only 1 item from the customer (1 antecedent)

# Time-based Analysis: Since your data spans multiple years, you might consider running the Apriori algorithm on a subset of the data based on time periods (e.g., monthly or yearly) to see if shopping patterns have changed over time.

# Customer Segmentation: You could also segment your customers based on certain characteristics or behaviors and run the Apriori algorithm for each segment to find more targeted association rules.

# Item Categorization: If your items can be categorized (e.g., dairy, fruits, beverages), you might consider running the algorithm on these categories instead of individual items for a higher-level view of associations.
