import flask
import pandas as pd
from flask import Flask
from flask_restplus import Api, Resource
import predictive_model
import documentation as doc
import os


app = Flask(__name__)
api = Api(
    app,
    version=doc.api['version'],
    title=doc.api['title'],
    description=doc.api['description'],
    doc='/swagger-ui.html'
)


predictive_model = predictive_model.load_model()


@api.route('/health')
@api.doc()
class HealthCheckResource(Resource):
    @api.response(200, 'Healthy')
    @api.response(500, 'Server Error')
    def get(self):
        """Health check endpoint"""
        if predictive_model is None:
            raise Exception("No predictive model")
        model_attributes = dir(predictive_model)
        if 'calculate_features' not in model_attributes:
            raise Exception("Lack of calculate_features method")
        if 'predict' not in model_attributes:
            raise Exception("Lack of predict method")
        return {"status": "success"}


prediction_request_model = api.model('PredictionRequest', doc.prediction_request_fields)
prediction_response_model = api.model('PredictionResponse', doc.prediction_response_fields)


@api.route('/prediction')
@api.doc()
class PredictionResource(Resource):

    @api.doc(
        params=doc.prediction_get_query_params,
        model='PredictionResponse'
    )
    def get(self):
        """Prediction endpoint"""
        # get request parameters
        raw_parameters = flask.request.args
        return PredictionResource._run_prediction(raw_parameters)

    @api.doc(
        body=prediction_request_model,
        model='PredictionResponse'
    )
    def post(self):
        """Prediction endpoint"""
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
    if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80, host='0.0.0.0')
    else:
        app.run(port=5000, host='0.0.0.0', debug=True)
