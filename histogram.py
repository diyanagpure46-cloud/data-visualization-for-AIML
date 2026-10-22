import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
