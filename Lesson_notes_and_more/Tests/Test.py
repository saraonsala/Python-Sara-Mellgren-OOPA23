import matplotlib.pyplot as plt
numbers = list(range(10))
squers = [number**2 for number in numbers]
print(numbers)
print (squers)

plt.plot(numbers, squers)
plt.title("x^2 for positive integers 0-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

