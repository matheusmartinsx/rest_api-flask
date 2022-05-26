from flask_restful import Resource, reqparse


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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('estado')
        
    def find_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel, 200
        return {'message':  'Hotel not found'}, 404
    
    def post(self, hotel_id):
        dados = self.argumentos.parse_args()
        
        novo_hotel = {'hotel_id': hotel_id, **dados}
        
        hoteis.append(novo_hotel)
        return novo_hotel, 200
    
    def put(self, hotel_id):
        dados = self.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def delete(self, hotel_id):
        pass