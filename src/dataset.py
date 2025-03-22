import pandas as pd

# 2. Cretaing a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

df.replace("Alice", "Alice Smith")
