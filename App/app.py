from flask import Flask, request, jsonify
import psycopg2
from db_connections.connections import session

from model.table import BMW_Vehicles

app = Flask(__name__)


@app.route('/get_all_vehicles', methods=['GET'])
def get_vehicles():
    vehicles = session.query(BMW_Vehicles).all()
    vehicles_list = [
        {'vehicle_id': vehicle.id, 'price': vehicle.price, 'model': vehicle.model, 'year': vehicle.year, 'color': vehicle.color} for
        vehicle in vehicles]
    return jsonify(vehicles_list)


@app.route('/add_vehicles', methods=['POST'])
def add_vehicle():
    new_vehicle_data = request.get_json()
    new_vehicle = BMW_Vehicles(
        id=new_vehicle_data['vehicle_id'],
        price=new_vehicle_data['price'],
        model=new_vehicle_data['model'],
        year=new_vehicle_data['year'],
        color=new_vehicle_data['color']
    )
    session.add(new_vehicle)
    session.commit()
    return jsonify({"message": "New vehicle added successfully"})


@app.route('/update_vehicles', methods=['PUT'])
def update_vehicle():
    user_data = request.get_json()
    session.query(BMW_Vehicles).filter(BMW_Vehicles.id == user_data.get('id')).update(user_data)

    session.commit()

    return jsonify({"message": "New vehicle updated successfully"})


@app.route('/delete_vehicles', methods=['DELETE'])
def delete_vehicle():
    data = request.get_json()
    session.query(BMW_Vehicles).filter(BMW_Vehicles.id == data.get('id')).delete()
    session.commit()
    return jsonify({"message": "New vehicle deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
