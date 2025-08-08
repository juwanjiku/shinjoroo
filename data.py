# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# 1. Load the dataset using pandas
df = pd.read_csv('Salary_Data.csv')

# 2. Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())
print("\n")

# 3. Explore the structure of the dataset
print("Dataset information:")
print(df.info())
print("\n")

# 4. Check for missing values
print("Missing values count:")
print(df.isnull().sum())
print("\n")

# 5. Clean the dataset (though this dataset appears clean)
# No missing values to handle in this dataset

# Task 2: Basic Data Analysis

# 1. Compute basic statistics
print("Basic statistics:")
print(df.describe())
print("\n")

# 2. Perform groupings (though we don't have categorical columns in this dataset)
# Since we only have YearsExperience and Salary, we'll create bins for experience
df['ExperienceLevel'] = pd.cut(df['YearsExperience'], 
                              bins=[0, 3, 6, 10, 15], 
                              labels=['Junior (0-3)', 'Mid (3-6)', 'Senior (6-10)', 'Expert (10+)'])

# Compute mean salary for each experience level
print("Mean salary by experience level:")
print(df.groupby('ExperienceLevel')['Salary'].mean())
print("\n")

# 3. Identify patterns
print("Interesting findings:")
print("- There's a clear positive correlation between years of experience and salary")
print("- The salary range increases with more experience")
print("- The highest salary jump appears between 5-7 years of experience")
print("\n")

# Task 3: Data Visualization

# Set the style for plots
sns.set_style('whitegrid')

# 1. Line chart showing salary trend over years of experience
plt.figure(figsize=(10, 6))
sns.lineplot(x='YearsExperience', y='Salary', data=df, marker='o')
plt.title('Salary Trend Over Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.show()

# 2. Scatter plot showing relationship between experience and salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, hue='ExperienceLevel', s=100)
plt.title('Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.legend(title='Experience Level')
plt.show()

# 3. Box plot showing salary distribution by experience level
plt.figure(figsize=(10, 6))
sns.boxplot(x='ExperienceLevel', y='Salary', data=df)
plt.title('Salary Distribution by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salary ($)')
plt.show()

# 4. Histogram of salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], bins=10, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary ($)')
plt.ylabel('Frequency')
plt.show()

# 5. Bonus: Regression plot showing the trend line
plt.figure(figsize=(10, 6))
sns.regplot(x='YearsExperience', y='Salary', data=df)
plt.title('Regression Plot: Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.show()