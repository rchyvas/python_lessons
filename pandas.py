import pandas as pd

data = {
    "name": ["john", "arthur", "anna", "diana"],
    "age": [66, 23, 54, 19],
    "city": ["athens", "tallinn", "helsinki", "riga"]
}

df = pd.DataFrame(data)
print(df)

