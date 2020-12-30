from matplotlib import pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 42, 4, 99, 102, 110, 120, 111, 125, 80, 75, 65, 54, 44, 43, 42, 48]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Histogram")

plt.show()