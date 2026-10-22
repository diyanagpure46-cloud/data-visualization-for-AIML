import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 55, 65, 75, 90]
}

sns.scatterplot(
    data=data,
    x="Study_Hours",
    y="Marks"
)

plt.title("Study Hours vs Marks")
plt.show()
