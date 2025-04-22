import pandas as pd # type: ignore
data = {
    'name': ['deepanshu', 'kevalya', 'om'],
    'age': [18, 19, 20],
    'city': ['uttarkashi', 'beawar', 'dehradun']
}
df = pd.DataFrame(data)
print("dataframe:\n", df)
print("describe:\n", df.describe())
print("access a column :\n", df['age'])
df.to_excel("data.xlsx", index=False)
