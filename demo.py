import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("student_marks.xlsx")
names = data["Name"]
marks = data["Marks"]

plt.figure(figsize=(14, 10))

plt.subplot(3, 3, 1)
plt.bar(names, marks)
plt.title("Bar Chart")

plt.subplot(3, 3, 2)
plt.plot(names, marks, marker="o")
plt.title("Line Chart")

plt.subplot(3, 3, 3)
plt.pie(marks, labels=names, autopct="%1.1f%%")
plt.title("Pie Chart")

plt.subplot(3, 3, 4)
plt.scatter(names, marks)
plt.title("Scatter Plot")

plt.subplot(3, 3, 5)
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Histogram")

plt.subplot(3, 3, 6)
plt.barh(names, marks)
plt.title("Horizontal Bar Chart")

plt.subplot(3, 3, 7)
plt.boxplot(marks)
plt.title("Box Plot")

plt.subplot(3, 3, 8)
plt.fill_between(range(len(marks)), marks)
plt.title("Area Plot")

plt.suptitle("Matplotlib Graphs Using Excel Data")
plt.tight_layout()
plt.show()
