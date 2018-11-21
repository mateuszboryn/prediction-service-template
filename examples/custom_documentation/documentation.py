from flask_restplus import fields


api = dict(
    version='1.0',
    title='Example Prediction Service with documentation',
    description='Example Prediction Service Description with documentation'
)

prediction_request_fields = {
    'x': fields.Float
}

prediction_get_query_params = {
    'x': 'value'
}

prediction_response_fields = {
    'prediction': fields.Float
}
