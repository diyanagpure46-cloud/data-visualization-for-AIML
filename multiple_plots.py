import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]
expenses = [80, 90, 100, 110]

plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o")
plt.title("Sales")

plt.subplot(1, 2, 2)
plt.bar(months, expenses)
plt.title("Expenses")

plt.tight_layout()
plt.show()
