import pandas as pd

data = {
    "name": ["john", "arthur", "anna", "diana"],
    "age": [66, 23, 54, 19],
    "city": ["vilnius", "klaipėda", "kaunas", "šilutė"]
}

df = pd.DataFrame(data)
print(df)

