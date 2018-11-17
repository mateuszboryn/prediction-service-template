import pickle
from sklearn import linear_model
import pandas as pd


# Model training:
training_data = pd.DataFrame([
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
    {'x': 3, 'y': 6},
    {'x': 4, 'y': 8}
])

model = linear_model.LinearRegression()
X_train = training_data[["x"]]
y_train = training_data[["y"]]
model.fit(X_train, y_train)
# TODO - serialize only model not this class
pickle.dump(model, open('model.pkl', 'wb'))
