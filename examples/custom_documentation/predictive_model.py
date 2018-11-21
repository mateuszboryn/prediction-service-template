import pickle


def load_model():
    return PredictiveModel(pickle.load(open('model.pkl', 'rb')))


class PredictiveModel:
    def __init__(self, model):
        self.model = model

    def predict(self, features):
        prediction = self.model.predict(features)
        # here you can add code to change response
        return {
            "prediction": prediction[0][0]
        }

    def calculate_features(self, raw_data):
        # here you can add your code for feature engineering
        features = raw_data.astype({"x": float})
        return features
