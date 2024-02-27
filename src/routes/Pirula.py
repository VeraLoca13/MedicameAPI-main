from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Pirula import Pirula
# Models
from models.PirulaModel import PirulaModel
# Utils
from utils.DateFormat import DateFormat

main = Blueprint('pirula_blueprint', __name__)


@main.route('/pirula/')
def get_pirulas():
    try:
        pirulas = PirulaModel.get_pirulas()
        return jsonify(pirulas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_pirula(id):
    try:
        pirula = PirulaModel.get_pirula(id)
        if pirula != None:
            return jsonify(pirula)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_pirula():
    try:
        name = request.json['name']
        brand = request.json['brand']
        dose = request.json['dose']
        type = request.json['type']
        amount_per_box = request.json['amount_per_box']
        with_food = request.json['with_food']
        without_food = request.json['without_food']
        with_other_pirula = request.json['with_other_pirula']
        current_quantity = request.json['current_quantity']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        pirula = pirula(0, name, brand, dose,  type, amount_per_box, with_food, without_food, with_other_pirula, current_quantity)

        affected_rows = PirulaModel.add_pirula(pirula)

        if affected_rows == 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_pirula(id):
    try:
        id = request.json['id']
        name = request.json['name']
        brand = request.json['brand']
        dose = request.json['dose']
        type = request.json['type']
        amount_per_box = request.json['amount_per_box']
        with_food = request.json['with_food']
        without_food = request.json['without_food']
        with_other_pirula = request.json['with_other_pirula']
        current_quantity = request.json['current_quantity']
        pirula = pirula(id, name, brand, dose,  type, amount_per_box, with_food, without_food, with_other_pirula, current_quantity)


        affected_rows = PirulaModel.update_pirula(pirula)

        if affected_rows == 1:
            return jsonify(pirula.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_pirula(id):
    try:
        pirula = pirula(id)

        affected_rows = PirulaModel.delete_pirula(pirula)

        if affected_rows == 1:
            return jsonify(pirula.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
