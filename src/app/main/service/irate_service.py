from typing import List, Any, Dict
from ..model.txn_tools import Transaction, ODCharges
from werkzeug.datastructures import FileStorage
import json

Data = List[Dict[str, Any]]
ResponseEnvelope = Dict[str, Any]

def create_od_summary(data: Data) -> ResponseEnvelope:
    try:
        od = ODCharges()
        od.transactions = list(filter(lambda x: x.description == od._od_marker,
                                     [Transaction(**t) for t in data]))
        resp_body: Data = []
        resp_envelope: ResponseEnvelope = dict()

        for rep in od.createSummary():
            name = rep.name
            data = rep.data
            response_data = {
                'name': name,
                'data': data
            }

            resp_body.append(response_data)

        resp_envelope['data'] = resp_body
        resp_envelope['status'] = 'success'
        resp_envelope['message'] = 'Summary complete'
        return resp_envelope, 200 # not 201 as no records created
    except Exception as e:
        response: ResponseEnvelope = {
                'status': 'fail',
                'message': 'Error creating overdraft summary report %r' % e,
                'data': []
            }


        return response, 500

def create_od_summary_from_file(file: FileStorage) -> ResponseEnvelope:
    # data = json.load(f).
    # unfortunately whole files are not json serializable with json.load...
    # so have had to load lines from the file
    data = []

    try:
        for line in file.stream.read().decode().split('\n'):
            if len(line):
                data.append(json.loads(line))
    except json.decoder.JSONDecodeError as e:
        response_data: ResponseEnvelope = {
                'status': 'fail',
                'message': 'Error reding json input %r' % e,
                'data': []
            }

        return response_data, 500
    return create_od_summary(data)
