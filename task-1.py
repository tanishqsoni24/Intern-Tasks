import pandas as pd

# Read the Excel file and set the data variable as a DataFrame
data = pd.read_excel('task_data.xlsx') 

# Convert 'date' column to datetime format for performing datetime operations
data['date'] = pd.to_datetime(data['date'])

# Extracting Week Number 
data['week'] = data['date'].dt.strftime('%Y-%W') 

# Grouping by week and calculating average price1
weekly_avg = data.groupby('week')['price1'].mean().reset_index()

# Naming the columns
weekly_avg.columns = ['week', 'average price'] 

# Saving the result to a new CSV file
weekly_avg.to_csv('task-1.csv', index=False)