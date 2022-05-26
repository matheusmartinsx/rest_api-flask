from flask_restful import Resource


hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'estado': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
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

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message':  'Hotel not found'}, 404
    
    def post(self, hotel_id):
        pass
    
    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass