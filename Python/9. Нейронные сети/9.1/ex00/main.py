#ОТВЕТ 1, держу в курсе
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X, y = X[:100], y[:100]
num_features = X.shape[1]
y = np.array([1 if y_i == 1 else -1 for y_i in y])


import random

random.seed(42)


class Perceptron:

    def __init__(self, num_features, nu, t_max):
        self.num_features = num_features
        self.nu = nu
        self.t_max = t_max

        self.w = np.zeros(self.num_features)
        self.b = 0

    def fit(self, X, y):
        t = 0
        while t <= self.t_max:
            r_index = random.randint(0, len(X) - 1)
            Xi, yi = X[r_index], y[r_index]
            if yi * self.predict(Xi) <= 0:
                self.b += self.nu * yi
                self.w += self.nu * yi * Xi
            t += 1

    def predict(self, X):
        X = np.atleast_2d(X)
        y = np.zeros(X.shape[0])

        for i in range(X.shape[0]):
            if sum(self.w * X[i, :]) + self.b >= 0:
                y[i] = +1
            else:
                y[i] = -1
        return y


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)
model = Perceptron(num_features, 0.1, 40)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = round(accuracy_score(y_test, y_pred), 2)


print("score {0:.2f}".format(score))