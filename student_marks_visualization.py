import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Student": ["Amit", "Priya", "Rahul", "Neha"],
    "Marks": [75, 92, 68, 85]
})

plt.bar(data["Student"], data["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.show()
