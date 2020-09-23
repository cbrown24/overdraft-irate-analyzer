import werkzeug
from flask import request, abort
from flask_restplus import Resource
from flask_restplus import reqparse

from ..service.irate_service import create_od_summary, create_od_summary_from_file
from ..util.dto import InterestRateDto

api = InterestRateDto.api
txn_meta = InterestRateDto.txn_meta
resp = InterestRateDto.response_envelope


file_upload = reqparse.RequestParser()
file_upload.add_argument('file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='Json file')

@api.route('/file/')
class ParseJsonFile(Resource):
    @api.expect(file_upload)
    @api.response(200, 'Calculation complete.')
    @api.marshal_list_with(resp)
    @api.doc('Perform a new calculation from json file')
    def post(self):
        """Perform a new calculation from json file"""
        args = file_upload.parse_args()
        file = args['file']
        return create_od_summary_from_file(file)


@api.route('/data/')
class ParseJsonData(Resource):
    @api.expect([txn_meta], validate=True)
    @api.response(200, 'Calculation complete.')
    @api.marshal_list_with(resp)
    @api.doc('Perform a new calculation from post payload')
    def post(self):
        """Perform a new calculation from post payload"""
        data = request.json
        return create_od_summary(data=data)

