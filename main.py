import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'Salary': [50000, 60000, 75000, 90000, 55000]}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate basic statistics
statistics = df.describe()

# Print the DataFrame and statistics
print("DataFrame:")
print(df)
print("\nStatistics:")
print(statistics)
