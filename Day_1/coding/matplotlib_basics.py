import matplotlib.pyplot as plt

# line chart

x = [1,2,3,4,5]
y = [15,20,25,30,35]

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.show()

# bar chart

subjects = ["Python","Java","C++","JavaScript"]
students = [45,30,15,40]

plt.bar(subjects, students)

plt.title("Students Learning Languages")
plt.xlabel("Programming Language")
plt.ylabel("Students")

plt.show()

# pie chart
labels = ["Python","Java","C++"]
sizes = [50,30,20]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Programming Languages")

plt.show()

# histogram
marks = [65,70,72,80,81,90,92,70,75,85]

plt.hist(marks)

plt.title("Marks Distribution")

plt.show()

# scatter plot
experience = [1,2,3,4,5,6,7,8]
salary = [25000,30000,35000,40000,45000,50000,55000,60000]

plt.scatter(experience, salary)

plt.title("Experience vs Salary")

plt.xlabel("Experience")

plt.ylabel("Salary")

plt.grid(True)

plt.show()

# to save chart
# plt.savefig("Day_1/images/plotting.png")