import pandas as pd

data = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80]
})

print("Dataset:")
print(data)

print("\nCorrelation:")
print(data.corr())
