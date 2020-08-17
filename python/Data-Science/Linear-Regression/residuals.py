import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)

X = boston[['RM']]
Y = boston['MEDV']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1)
model = LinearRegression()
y_test_predicted = model.predict(X_test)
plt.scatter(X_test, Y_test,
  label='testing data');
plt.plot(X_test, y_test_predicted,
  label='prediction', linewidth=3)
plt.xlabel('RM'); plt.ylabel('MEDV')
plt.legend(loc='upper left')
plt.show()