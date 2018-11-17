import flask
import pandas as pd
from flask import Flask
from flask_restplus import Api, Resource
import predictive_model


app = Flask(__name__)
# TODO - allow customization
api = Api(app, version='1.0', title='Prediction Service', description='Prediction Service Description')


predictive_model = predictive_model.load_model()


@api.route('/health')
@api.doc()
class HealthCheckResource(Resource):
    def get(self):
        if predictive_model is None:
            raise Exception("No predictive model")
        model_attributes = dir(predictive_model)
        if 'calculate_features' not in model_attributes:
            raise Exception("Lack of calculate_features method")
        if 'predict' not in model_attributes:
            raise Exception("Lack of predict method")
        return {"status": "success"}


# TODO - allow api doc customization
@api.route('/prediction')
@api.doc()
class PredictionResource(Resource):
    def get(self):
        # get request parameters
        raw_parameters = flask.request.args
        return PredictionResource._run_prediction(raw_parameters)

    def post(self):
        # get request parameters
        raw_parameters = flask.request.form
        return PredictionResource._run_prediction(raw_parameters)

    @staticmethod
    def _run_prediction(raw_parameters):
        # create data frame
        raw_data = pd.DataFrame([raw_parameters.to_dict()])
        # feature engineering
        features = predictive_model.calculate_features(raw_data)
        # run prediction
        return predictive_model.predict(features)


if __name__ == '__main__':
    app.run(debug=True)
