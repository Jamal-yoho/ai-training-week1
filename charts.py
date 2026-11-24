import matplotlib.pyplot as plt               # Chart create
import pandas as pd                           # Read csv file

df = pd.read_csv("employees.csv")
print(df)

#Average salary

avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)

# bar chart of average salary per department with title, axis labels and values on the bars

bars = plt.bar(avg_salary.index,avg_salary.values)
plt.bar_label(bars)
plt.title("Average Salary By Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.savefig("bar_chart.png")
plt.show()

# histogram of salaries with 5 bins
salary = df["salary"]
plt.hist(salary, bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employee")
plt.savefig("histogram.png")
plt.show()

# scatter plot of id vs salary coloured by department with a legend

for dept in df["department"].unique():
    dept_data = df[df["department"] == dept]
    plt.scatter(dept_data["id"],dept_data["salary"],label=dept)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.savefig("Scatter_plot.png")
plt.show()

# line chart of this monthly sales list with markers: 12, 15, 14, 18, 22, 25 (Jan to Jun) and
#save every chart as a PNG
months = ["Jan","Feb", "Mar", "Apr", "May", "Jun"]
sales =[12, 15, 14, 18, 22, 25]

plt.plot(months,sales, marker=0)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.savefig("Line_chart.png")
plt.show()

