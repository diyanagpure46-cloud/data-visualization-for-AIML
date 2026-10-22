import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Python": [85, 90, 78],
    "Maths": [75, 80, 88],
    "AI": [90, 85, 92]
})

correlation = data.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Subject Correlation Heatmap")
plt.show()
