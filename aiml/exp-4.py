import pandas as pd
filein = 'input.csv'
try:
    df = pd.read_csv(filein)
    print(f"data imported successfully from '{filein}'")
except FileNotFoundError:
    print(f"File '{filein}' not found.")
    exit()
print("dataset details:")
print(f"number of rows: {df.shape[0]}")
print(f"number of columns: {df.shape[1]}")
print(f"size of data set (product of rows and columns) {df.size}")
print("First 5 Rows:")
print(df.head())
print("Missing Values in Each Column:")
print(df.isnull().sum())
print("Summary Statistics (Numerical Columns):")
numericals = df.select_dtypes(include='number')
if not numericals.empty:
    print("sum:")
    print(numericals.sum())
    print("avg:")
    print(numericals.mean())
    print("Min:")
    print(numericals.min())
    print("max:")
    print(numericals.max())
else:
    print("No numerical columns found in the dataset.")
fileout = 'output.csv'
df.to_csv(fileout, index=False)
print(f"Data exported successfully to '{fileout}'")
