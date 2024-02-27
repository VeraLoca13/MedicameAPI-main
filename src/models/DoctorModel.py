from database.db import get_connection
from .entities.Doctors import Doctors


class DoctorsModel():

    @classmethod
    def get_doctors(self):
        try:
            connection = get_connection()
            doctors = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, medical_speciality, name, ocupation, age, shift FROM doctors ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    Doctors = Doctors(row[0], row[1], row[2], row[3], row[4], row[5])
                    doctors.append(Doctors.to_JSON())

            connection.close()
            return doctors
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_doctor(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, medical_speciality, name, ocupation, age, shift FROM Doctors WHERE id = %s", (id,))
                row = cursor.fetchone()

                Doctors = None
                if row != None:
                    Doctors = Doctors(row[0], row[1], row[2], row[3], row[4], row[5])
                    Doctors = Doctors.to_JSON()

            connection.close()
            return Doctors
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_doctor(self, doctor):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO Doctors (medical_speciality, name, ocupation, age, shift) 
                                VALUES ( %s, %s, %s, %s, %s)""", (doctor.medical_speciality, doctor.name, doctor.ocupation, doctor.age, doctor.shift))
                affected_rows = cursor.rowcount
                
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_doctor(self, doctor):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE Doctors SET medical_speciality = %s, name = %s, ocupation = %s, age = %s, shift = %s 
                                WHERE id = %s""", (doctor.medical_speciality, doctor.name, doctor.ocupation, doctor.age, doctor.shift))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_doctor(self, doctor):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Doctors WHERE id = %s", (doctor.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
