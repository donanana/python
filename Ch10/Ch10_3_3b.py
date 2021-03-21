import matplotlib.pyplot as plt

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("Day")
plt.ylabel("Celsius")
plt.xticks(range(0, 25, 2))
plt.yticks(range(15, 35, 3))
plt.show()

