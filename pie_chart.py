import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "DSA", "AI"]
marks = [85, 78, 92, 88]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%"
)
plt.title("Marks Distribution")
plt.show()
