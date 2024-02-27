from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Treatment import Treatment
# Models
from models.TreatmentModel import TreatmentModel
# Utils
from utils.DateFormat import DateFormat

main = Blueprint('treatment_blueprint', __name__)


@main.route('/treatment/')
def get_treatments():
    try:
        treatments = TreatmentModel.get_treatments()
        return jsonify(treatments)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_treatment(id):
    try:
        treatment = TreatmentModel.get_treatment(id)
        if treatment != None:
            return jsonify(treatment)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_treatment():
    try:
        pirula_name = request.json['pirulaName']
        start_date = request.json['startDate']
        end_date = request.json['endDate']
        frecuency = request.json['frecuency']
        first_dose = request.json['firstDose']
        last_dose = request.json['lastDose']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        treatment = treatment(0, pirula_name, start_date, end_date,  frecuency, first_dose, last_dose)

        affected_rows = TreatmentModel.add_treatment(treatment)

        if affected_rows == 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_treatment(id):
    try:
        id = request.json['id']
        pirula_name = request.json['pirulaName']
        start_date = request.json['startDate']
        end_date = request.json['endDate']
        frecuency = request.json['frecuency']
        first_dose = request.json['firstDose']
        last_dose = request.json['lastDose']
        treatment = treatment(id, pirula_name, start_date, end_date,  frecuency, first_dose, last_dose)


        affected_rows = TreatmentModel.update_treatment(treatment)

        if affected_rows == 1:
            return jsonify(treatment.id)
        else:
            return jsonify({'message': "No treatment updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_treatment(id):
    try:
        treatment = treatment(id)

        affected_rows = TreatmentModel.delete_treatment(treatment)

        if affected_rows == 1:
            return jsonify(treatment.id)
        else:
            return jsonify({'message': "No treatment deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
