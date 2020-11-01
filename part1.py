import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([0, 0.050, 0.100, 0.150, 0.200, 0.250, 0.300]).reshape((-1, 1))
y = np.array([0, 0.08, 0.165, 0.245, 0.325, 0.41, 0.49])

reg = LinearRegression()
reg.fit(x, y)

print("The equation for the line of best fit: L(x) = {} * x + {}".format(reg.coef_[0], reg.intercept_))

# Plot outputs
plt.scatter(x, y,  color='black')
plt.plot(x, reg.predict(x), color='blue', linewidth=3)

plt.show()
