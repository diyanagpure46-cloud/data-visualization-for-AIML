import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "DSA", "AI"]
marks = [85, 78, 92, 88]

plt.bar(subjects, marks)
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
