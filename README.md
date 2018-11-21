# prediction-service-template

Template for deploying prediction services as REST API

# Build and run sample

    docker build . -t prediction-service-template
    docker run  --rm -it -p 80:80 prediction-service-template

Go to:

    http://localhost/prediction?x=2
    
# Examples

[examples](examples)

# Endpoints

## Swagger documentation

[/swagger-ui.html](http://localhost:5000/swagger-ui.html)

## Health check

[/health](http://localhost:5000/health)

## Prediction

[/prediction](http://localhost:5000/prediction?x=1)

# Customizations

## Custom prediction model

Prediction model should be provided in file **model.pkl**

Model should be serialized in below way:

    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    pickle.dump(model, open('model.pkl', 'wb'))

## Custom feature engineering

Feature engineering should be provided in file **predictive_model.py**

There should be Pyton class returned by method **load_model()** which has method **calculate_features(self, raw_data)**

Input to this method is Pandas DataFrame

```python
import pickle


def load_model():
    return PredictiveModel(pickle.load(open('model.pkl', 'rb')))


class PredictiveModel:
    def __init__(self, model):
        self.model = model
        
    def calculate_features(self, raw_data):
        # here you can add your code for feature engineering
        features = raw_data.astype({"x": float})
        return features
```

## Custom response

API response should be provided in **predict(self, features)** method, where **features** is Pandas DataFrame.

This is output of **calculate_features()** method.

```python

class PredictiveModel:
    def __init__(self, model):
        self.model = model
        
    def predict(self, features):
        prediction = self.model.predict(features)
        # here you can add code to change response
        return {
            "prediction": prediction[0][0]
        }
```

## Custom documentation

Custom documentation should be provided in file **documentation.py**

### Basic information

```python
api = dict(
    version='1.0',
    title='Prediction Service Template',
    description='Prediction Service Description'
)
```

### Request and response 

```python
from flask_restplus import fields

prediction_request_fields = {
    'x': fields.Float
}

prediction_get_query_params = {
    'x': 'value'
}

prediction_response_fields = {
    'prediction': fields.Float
}
```
