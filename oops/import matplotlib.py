import matplotlib.pyplot as plt
import numpy as np
students = ["Arun","sapp","Appu","sam","grace"]
marks = [80,90,70,85,95]
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.show()
#pie chart
labels = ["Arun","sapp","Appu","sam","grace"]
sizes = [80,90,70,85,95]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()
#scatter plot
x = [1, 2, 3, 4, 5] 
y = [80, 90, 70, 85, 95]
plt.scatter(x, y)
plt.xlabel("Student Number")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.show()

