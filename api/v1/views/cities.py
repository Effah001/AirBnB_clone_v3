#!/usr/bin/python3
"""State module"""
from flask import jsonify, request, abort, make_response
from models.city import City
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """Retrieves the list of cities for a state id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    list_cities = [obj.to_dict() for obj in state.cities]
    return jsonify(list_cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a city"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashed=False)
def delete_city(city_id):
    """Deletes a State object"""
    city = storage.get(City, city_id)
    if city:
        city.delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Creates a new city"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    new_city = City(**data)
    storage.new(new_City)
    storage.save()
    return jsonify(new_City.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_state(city_id):
    """Updates a city object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for key, value in data.items():
        if key not in ['id', 'state_created', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
