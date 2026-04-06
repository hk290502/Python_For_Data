import pandas as pd

import numpy as np

temp_df = pd.read_excel(r'C:\WiseOwl\overview_of_numpy\Purchases.xlsx')

for col in temp_df.columns[1:]:
    temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')

temp_df = temp_df.fillna(0)

purchases = np.asarray(temp_df.iloc[0:4, 1:6])

volumes = purchases.astype(float)
new_volumes = volumes.astype('i1')


print("Data type:", new_volumes.dtype)

prices = np.array([[2, 1, 1.5, 1.5]])


print("\nPrices shape:", prices.shape)
print("New volumes shape:", new_volumes.shape)


spending_per_day = np.dot(prices, new_volumes)
print("\nSpending per day")
print("=" * 16)
print(spending_per_day)

total_spending = spending_per_day.sum()
print("\nTotal spending")
print("=" * 14)
print(total_spending)