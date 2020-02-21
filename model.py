import numpy as np
from sklearn import datasets, linear_model, metrics
import pickle

boston = datasets.load_boston(return_X_y=False)
X = boston.data
y = boston.target
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('Coefficients: \n', reg.coef_)
print("score: ", reg.score(X_test, y_test))
filename = "model.pkl"
pickle.dump(reg, open(filename,'wb'))
