import pandas as pd

# Load the CSV file
df = pd.read_csv('sample_data.csv')

# 1. Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# 2. Display basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# 3. Show summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# 4. Count the number of missing values in each column
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# 5. Filter the data for people with salary > 50,000
high_salary = df[df['Salary'] > 50000]
print("\nPeople with a salary greater than 50,000:")
print(high_salary)

# 6. Group data by 'Country' and calculate the average salary
grouped_data = df.groupby('Country')['Salary'].mean()
print("\nAverage salary by country:")
print(grouped_data)
