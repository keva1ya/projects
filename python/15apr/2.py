from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]
plt.plot(x, y, marker='o')
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()