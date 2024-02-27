from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.VisitaMedica import VisitaMedica
# Models
from models.VisitaMedicaModel import VisitaMedicaModel
# Utils
from utils.DateFormat import DateFormat

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_visitas():
    try:
        visitas = VisitaMedicaModel.get_visitas()
        return jsonify(visitas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_visita(id):
    try:
        visita = VisitaMedicaModel.get_visita(id)
        if visita != None:
            return jsonify(visita)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_visita():
    try:
        especialidad = request.json['especialidad']
        doctor = request.json['doctor']
        lugar = request.json['lugar']
        fecha = request.json['fecha']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        visita = VisitaMedica(0,especialidad, doctor, lugar, DateFormat.convert_str_date(fecha), DateFormat.convert_str_date(fecha))

        affected_rows = VisitaMedicaModel.add_visita(visita)

        if affected_rows == 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_visita(id):
    try:
        especialidad = request.json['especialidad']
        doctor = request.json['doctor']
        lugar = request.json['lugar']
        fecha = request.json['fecha']
        visita = VisitaMedica(id, especialidad, doctor, lugar, DateFormat.convert_str_date(fecha), DateFormat.convert_str_date(fecha))


        affected_rows = VisitaMedicaModel.update_visita(visita)

        if affected_rows == 1:
            return jsonify(visita.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_visita(id):
    try:
        visita = VisitaMedica(id)

        affected_rows = VisitaMedicaModel.delete_visita(visita)

        if affected_rows == 1:
            return jsonify(visita.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
