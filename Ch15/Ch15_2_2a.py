import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

temperatures = np.array([29, 28, 34, 31,
                         25, 29, 32, 31,
                         24, 33, 25, 31,
                         26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4,
                        5.9, 6.4, 8.0, 7.5,
                        5.8, 9.1, 5.1, 7.3,
                        6.5, 8.4])
X = pd.DataFrame(temperatures, columns=["Temperature"])
target = pd.DataFrame(drink_sales, columns=["Drink_Sales"])
y = target["Drink_Sales"]
lm = LinearRegression()
lm.fit(X, y)
# 預測氣溫26, 30度的業績
new_temperatures = pd.DataFrame(np.array([26, 30]))
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)

plt.scatter(temperatures, drink_sales)  # 繪點
regression_sales = lm.predict(X)
plt.plot(temperatures, regression_sales, color="blue")
plt.plot(new_temperatures, predicted_sales, 
         color="red", marker="o", markersize=10)
plt.show()