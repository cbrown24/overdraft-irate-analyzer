from flask_restplus import Namespace, fields

class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'

class InterestRateDto:
    api = Namespace('overdraft', description='Create Overdraft Report')
    txn_meta = api.model('txn_meta', {
        "amount":  fields.Float(required=False),
        "description": NullableString(required=False),
        "timestamp": fields.DateTime(),
        "balance": fields.Float(required=False),
    })
    response_meta = api.model('response_meta', {
        "date": fields.Date(),
        "value": fields.Float(required=True),
    })
    response = api.model('response', {
        "name": fields.String(require=False),
        "data": fields.List(fields.Nested(response_meta)),
    })
    response_envelope = api.model('response', {
        "status": fields.String(require=False),
        "message": fields.String(require=False),
        "data": fields.List(fields.Nested(response, skip_none=True))
    })
