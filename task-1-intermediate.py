import pandas as pd

# Read the input file
input_file = 'AVW.xls'
df = pd.read_excel(input_file)

# Calculate column D
df['Change'] = df['Input'].diff()

# Calculate column E
df['Gain'] = df['Change'].apply(lambda x: x if x > 0 else 0)

# Calculate column F
df['Loss'] = df['Change'].apply(lambda x: abs(x) if x < 0 else 0)

# Calculate column G
df['Avg Gain'] = df['Gain'].rolling(window=14).mean()

# Calculate column H
df['Avg Loss'] = df['Loss'].rolling(window=14).mean()

# Calculate column I
df['HM'] = df['Avg Gain'] / df['Avg Loss']

# Write the changes back to the input file
df.to_excel("intermediete.xlsx", index=False)
