import pandas as pd

# Read the Excel file and set the data variable as a DataFrame
data = pd.read_excel('task_data.xlsx')

# Create a new column 'choice' based on the condition price1 > price2
data['choice'] = ['R' if price1 > price2 else 'G' for price1, price2 in zip(data['price1'], data['price2'])] #LIST COMPREHENSION

result_rows = []

# Iterate over the rows of the DataFrame
for i in range(len(data) - 2):
    # Check if three consecutive rows have the condition price1 > price2
    if data.loc[i, 'choice'] == 'R' and data.loc[i + 1, 'choice'] == 'R' and data.loc[i + 2, 'choice'] == 'R':
        # Check if the middle row has the lowest price2 value among the three
        if data.loc[i + 1, 'price2'] == min(data.loc[i, 'price2'], data.loc[i + 1, 'price2'], data.loc[i + 2, 'price2']):
            # Store the rows that satisfy the condition
            result_rows.append(data.loc[i:i+2])

# Concatenate the stored rows into a new DataFrame
result = pd.concat(result_rows)

# Print the resulting DataFrame
result.to_csv('task-2.csv', index=False)