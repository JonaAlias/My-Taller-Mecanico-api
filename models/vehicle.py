from models.db import db

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    plate = db.Column(db.String(15), unique=True, nullable=False)
    
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, brand, model, year, plate, client_id):
        self.brand = brand
        self.model = model
        self.year = year
        self.plate = plate
        self.client_id = client_id

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'plate': self.plate,
            'client_id': self.client_id
        }
