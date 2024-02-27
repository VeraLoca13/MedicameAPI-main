from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Doctors import Doctors
# Models
from models.DoctorModel import DoctorModel
# Utils
from utils.DateFormat import DateFormat

main = Blueprint('doctor_blueprint', __name__)


@main.route('/')
def get_Doctors():
    try:
        Doctors = DoctorModel.get_Doctors()
        return jsonify(Doctors)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_doctor(id):
    try:
        doctor = DoctorModel.get_doctor(id)
        if doctor != None:
            return jsonify(doctor)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_doctor():
    try:
        medical_speciality = request.json['medicalSpeciality']
        name = request.json['name']
        ocupation = request.json['ocupation']
        age = request.json['age']
        shift = request.json['shift']
        #Generar id de texto unico basado en el tiempo
        #id = uuid.uuid4()
        doctor = Doctors(0,medical_speciality, name, ocupation, DateFormat.convert_str_date(age), DateFormat.convert_str_date(shift))

        affected_rows = DoctorModel.add_doctor(doctor)

        if affected_rows == 1:
            return jsonify(affected_rows)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_doctor(id):
    try:
        medical_speciality = request.json['medical_speciality']
        name = request.json['name']
        ocupation = request.json['ocupation']
        age = request.json['age']
        shift = request.json['shift']
        doctor = Doctors(id, medical_speciality, name, ocupation, DateFormat.convert_str_date(age), DateFormat.convert_str_date(shift))


        affected_rows = DoctorModel.update_doctor(doctor)

        if affected_rows == 1:
            return jsonify(doctor.id)
        else:
            return jsonify({'message': "No doctor updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_doctor(id):
    try:
        doctor = Doctors(id)

        affected_rows = DoctorModel.delete_doctor(doctor)

        if affected_rows == 1:
            return jsonify(doctor.id)
        else:
            return jsonify({'message': "No doctor deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
