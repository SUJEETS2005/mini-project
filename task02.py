import matplotlib.pyplot as plt
years=[2019,2020,2021,2022,2023]
users=[50,65,80,95,110]
fig, ax = plt.subplots()
ax.plot(years,users,label="Internet Users Growth")
ax.set_xlabel("Year")
ax.set_ylabel("Users (Millions)")
ax.set_title("Internet Users Growth Over Years")
ax.legend()
ax.grid()
plt.savefig("graph1.png")
plt.show()

months=[1,2,3,4,5]
app1=[200,300,400,500,600]
app2=[150,250,350,450,550]
fig, ax = plt.subplots()
ax.plot(months,app1,label="App A")
ax.plot(months,app2,label="App B")
ax.set_title("App Download Comparison")
ax.legend()
ax.grid()
plt.savefig("graph2.png")
plt.show()

practice=[1,2,3,4,5]
skill=[40,50,65,80,95]
fig, ax = plt.subplots()
ax.scatter(practice,skill,label="Coding Data")
ax.set_xlabel("Practice Hours")
ax.set_ylabel("Skill Score")
ax.set_title("Coding Practice vs Skill")
ax.legend()
plt.savefig("graph3.png")
plt.show()

departments=["CSE","ECE","MECH"]
placements=[120,90,60]
fig, ax = plt.subplots()
ax.bar(departments,placements,label="Placements")
ax.set_title("Department Placement Count")
ax.set_ylabel("Students Placed")
ax.legend()
plt.savefig("graph4.png")
plt.show()

prices=[40000,45000,50000,55000,60000,42000,48000,52000,58000]
fig, ax = plt.subplots()
ax.hist(prices,bins=5,label="Laptop Prices")
ax.set_title("Laptop Price Distribution")
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
ax.legend()
plt.savefig("graph5.png")
plt.show()

brands=["Samsung","Apple","Xiaomi","OnePlus"]
share=[35,30,20,15]
fig, ax = plt.subplots()
ax.pie(share,labels=brands,autopct='%1.1f%%')
ax.set_title("Smartphone Market Share")
plt.savefig("graph6.png")
plt.show()

fig, ax = plt.subplots(1,2)
days=[1,2,3,4]
temperature=[30,32,34,33]
ax[0].plot(days,temperature,label="Temperature")
ax[0].set_title("Temperature Trend")
ax[0].legend()
ax[1].scatter(days,temperature,label="Temp Data")
ax[1].set_title("Temperature Scatter")
ax[1].legend()
plt.savefig("graph7.png")
plt.show()

fig, ax = plt.subplots(1,3,figsize=(12,4))
x=[1,2,3,4]
y=[10,20,30,40]
ax[0].plot(x,y)
ax[0].set_title("Line Plot")
courses=["Python","Java","C++"]
students=[40,35,25]
ax[1].bar(courses,students)
ax[1].set_title("Course Enrollment")
data=[5,10,15,20,25]
ax[2].hist(data)
ax[2].set_title("Data Distribution")
plt.show()

fig, ax = plt.subplots(2,1)
days=[1,2,3,4]
sales1=[100,150,200,250]
sales2=[80,120,160,220]
ax[0].plot(days,sales1,label="Store 1")
ax[0].set_title("Store 1 Sales")
ax[0].legend()
ax[0].grid()
ax[1].plot(days,sales2,label="Store 2")
ax[1].set_title("Store 2 Sales")
ax[1].legend()
ax[1].grid()
plt.tight_layout()
plt.savefig("graph8.png")
plt.show()