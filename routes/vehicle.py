from flask import Blueprint, jsonify, request
from models.vehicle import Vehicle
from models.db import db

vehicle = Blueprint('vehicle', __name__)

# Obtener todos los vehículos
@vehicle.route('/api/vehicle', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([v.serialize() for v in vehicles]), 200

# Obtener vehículo por ID
@vehicle.route('/api/vehicle/<int:id>', methods=['GET'])
def get_vehicle_by_id(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({'error': 'Vehículo no encontrado'}), 404
    return jsonify(vehicle.serialize()), 200

# Crear nuevo vehículo
@vehicle.route('/api/vehicle', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    try:
        new_vehicle = Vehicle(
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            plate=data['plate'],
            client_id=data['client_id']
        )
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify(new_vehicle.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Actualizar vehículo
@vehicle.route('/api/vehicle/<int:id>', methods=['PUT'])
def update_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({'error': 'Vehículo no encontrado'}), 404
    data = request.get_json()
    vehicle.brand = data.get('brand', vehicle.brand)
    vehicle.model = data.get('model', vehicle.model)
    vehicle.year = data.get('year', vehicle.year)
    vehicle.plate = data.get('plate', vehicle.plate)
    vehicle.client_id = data.get('client_id', vehicle.client_id)
    db.session.commit()
    return jsonify(vehicle.serialize()), 200

# Eliminar vehículo
@vehicle.route('/api/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return jsonify({'error': 'Vehículo no encontrado'}), 404
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehículo eliminado'}), 200
