from flask import Flask, request, json, Response
from flask_restful import Resource, Api, fields
import datetime

app = Flask(__name__)
api = Api(app)

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)

def api_response(status, data=None):
    return Response(
        json.dumps(data, cls=CustomJsonEncoder),
        status=status,
        mimetype="application/json"
    )

class Bcfm(Resource):
    def get(self):
        return api_response(200, list({'message': 'BCFM'}))

api.add_resource(Bcfm, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
