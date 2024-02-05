import matplotlib.pyplot as plt
numbers = list(range(10))
squers = [number**2 for number in numbers]
print(numbers)
print (squers)

plt.plot(numbers, squers)
plt.show()

