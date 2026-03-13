import matplotlib.pyplot as plt
sleep_hours = [4,5,6,7,8]
productivity = [50,55,65,75,85]
plt.scatter(sleep_hours, productivity, color="red")
plt.title("Sleep Hours vs Productivity")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")
plt.savefig("sleep_scatter.png")
plt.show()

departments = ["CSE", "ECE", "MECH", "CIVIL"]
students = [120, 100, 80, 60]
plt.bar(departments, students, color="blue")
plt.title("Students in Each Department")
plt.xlabel("Departments")
plt.ylabel("Number of Students")
plt.savefig("department_bar.png")
plt.show()

marks = [65,70,75,80,85,90,60,55,72,88,77,69]
plt.hist(marks, bins=5, color="green", edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("marks_histogram.png")
plt.show()

brands = ["Samsung","Apple","OnePlus","Xiaomi"]
users = [35,30,20,15]
plt.pie(users, labels=brands, autopct="%1.1f%%")
plt.title("Mobile Brand Usage")
plt.savefig("mobile_pie.png")
plt.show()