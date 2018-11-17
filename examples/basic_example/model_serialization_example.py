import pickle
from sklearn import linear_model
import pandas as pd
import predictive_model


# Model training:
training_data = pd.DataFrame([
    {'x': 1, 'y': 3},
    {'x': 2, 'y': 6},
    {'x': 3, 'y': 9},
    {'x': 4, 'y': 12}
])

model = linear_model.LinearRegression()
X_train = training_data[["x"]]
y_train = training_data[["y"]]
model.fit(X_train, y_train)
pickle.dump(predictive_model.PredictiveModel(model), open('model.pkl', 'wb'))
