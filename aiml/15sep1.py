import pandas as pd
data_dict = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [23, 27, 22]
}

df_from_dict = pd.DataFrame(data_dict)

print(df_from_dict)