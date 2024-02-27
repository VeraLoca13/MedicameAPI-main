from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Pirula import Pirula
# Models
from models.PirulaModel import PirulaModel
# Utils
from utils.DateFormat import DateFormat

main = Blueprint('movie_blueprint', __name__)


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
        amountPerBox = request.json['amountPerBox']
        withFood = request.json['withFood']
        withoutFood = request.json['withoutFood']
        withOtherPirula = request.json['withOtherPirula']
        currentQuantity = request.json['currentQuantity']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        pirula = pirula(0, name, brand, dose,  type, amountPerBox, withFood, withoutFood, withOtherPirula, currentQuantity)

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
        amountPerBox = request.json['amountPerBox']
        withFood = request.json['withFood']
        withoutFood = request.json['withoutFood']
        withOtherPirula = request.json['withOtherPirula']
        currentQuantity = request.json['currentQuantity']
        pirula = pirula(id, name, brand, dose,  type, amountPerBox, withFood, withoutFood, withOtherPirula, currentQuantity)


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
