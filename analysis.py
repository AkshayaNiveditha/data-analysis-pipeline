# Data Analysis Pipeline

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Name": ["Manoj", "Akshaya", "Ravi"],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

# Basic analysis
print("Summary:")
print(df.describe())

# Visualization
df.plot(x="Name", y="Score", kind="bar")
plt.title("Scores")
plt.show()