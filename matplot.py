import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y1 = [12,24,36,48,60]
y2 = [8,18,28,38,48]

plt.figure(figsize=(8,5), dpi=100)

plt.plot(x, y1, color="blue", linestyle="-", linewidth=2, marker="o", markersize=7)
plt.plot(x, y2, color="green", linestyle="--", linewidth=3, marker="*", markersize=15)

plt.annotate(
    "Highest Point",
    xy=(10,60),
    xytext=(6,60),
    arrowprops=dict(facecolor="grey")
)
plt.xlabel("X Axis Values")
plt.ylabel("Y Axis Values")
plt.title("Sample Matplotlib Graph")

plt.legend(["Blue Line","Green Line"])
plt.grid(True)

plt.savefig("new_graph.jpg")
plt.show()