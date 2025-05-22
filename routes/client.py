from flask import Blueprint, jsonify, request
from models.client import Client
from models.db import db

client = Blueprint('client', __name__)

# Obtener todos los clientes
@client.route('/api/client', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients]), 200

# Obtener cliente por ID
@client.route('/api/client/<int:id>', methods=['GET'])
def get_client_by_id(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Cliente no encontrado'}), 404
    return jsonify(client.serialize()), 200

# Crear nuevo cliente
@client.route('/api/client', methods=['POST'])
def create_client():
    data = request.get_json()
    try:
        new_client = Client(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(new_client)
        db.session.commit()
        return jsonify(new_client.serialize()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Actualizar cliente
@client.route('/api/client/<int:id>', methods=['PUT'])
def update_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Cliente no encontrado'}), 404
    data = request.get_json()
    client.name = data.get('name', client.name)
    client.email = data.get('email', client.email)
    client.phone = data.get('phone', client.phone)
    db.session.commit()
    return jsonify(client.serialize()), 200

# Eliminar cliente
@client.route('/api/client/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'error': 'Cliente no encontrado'}), 404
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado'}), 200
