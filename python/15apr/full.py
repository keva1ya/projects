import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

data = {
    'Name': ['kevalya', 'badri', 'suryansh', 'deepanshu', 'avishi'],
    'Age': [19, 18, 19, 18, 19],
    'Salary': [500, 600, 55, 750, 6800]
}

df = pd.DataFrame(data)
print(df)

print("\nAverage Age:", df['Age'].mean())
print("\nSalary Statistics:")
print(df['Salary'].describe())

print("\nPeople with Salary > 600:")
print(df[df['Salary'] > 600])

df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus Column:")
print(df)

print("\nIndex of 'kevalya':")
print(df[df['Name'] == 'kevalya'].index)

# Save the salary data to an Excel sheet
df[['Name', 'Salary']].to_excel('salaries.xlsx', index=False)
print("\nSalary data has been saved to 'salaries.xlsx'.")

arr = np.array([1, 2, 3, 4, 5])
print("\nNumPy array:", arr)

arr_square = np.square(arr)
print("\nSquared array:", arr_square)

arr2d = np.array([[1, 2], [3, 4]])
arr2d_mult = np.dot(arr2d, arr2d)
print("\nMatrix multiplication result:")
print(arr2d_mult)

plt.figure(figsize=(8, 5))
plt.plot(df['name'], df['salary'], label='salary', marker='o')
plt.title('Employee v/s salary')
plt.xlabel('Employee name')
plt.ylabel('salary')
plt.grid(True)
plt.legend()
plt.show()