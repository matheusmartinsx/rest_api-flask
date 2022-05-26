from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'estado': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 4.0,
        'diaria': 400.10,
        'estado': 'Santa Catarina'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 385.60,
        'estado': 'Santa Catarina'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
    
#http://127.0.0.1:5000/hoteis