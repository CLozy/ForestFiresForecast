from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np
#X with 5rows and 2columns from 0-9 y is 5columns from range 0-4
#X array represents features y array represents values we want to estimate
X, y = np.arange(10).reshape((5, 2)), range(5)
print("Testing with random_state=None and shuffle=False")
#split data with test set of 33% which is 2rows
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,shuffle=False)
print("--X-Train--")
print(X_train)
print("--X-Test--")
print(X_test)
print("--Y-Train--")
print(y_train)
print("--Y-Test--")
print(y_test)