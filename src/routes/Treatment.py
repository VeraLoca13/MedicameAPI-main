from flask import Blueprient, jsonify, request
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
        treatments = treatmentModel.get_treatments()
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
        pirula_name = request.json['pirula_name']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        frecuency = request.json['frecuency']
        first_dose = request.json['first_dose']
        last_dose = request.json['last_dose']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        treatment = treatment(0, name, start_date, end_date,  frecuency, first_dose, last_dose)

        affected_rows = treatmentModel.add_treatment(treatment)

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
        name = request.json['name']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        frecuency = request.json['frecuency']
        first_dose = request.json['first_dose']
        last_dose = request.json['last_dose']
        treatment = treatment(id, name, start_date, end_date,  frecuency, first_dose, last_dose)


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
