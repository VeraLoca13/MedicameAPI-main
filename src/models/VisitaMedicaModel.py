from database.db import get_connection
from .entities.VisitaMedica import VisitaMedica


class VisitaMedicaModel():

    @classmethod
    def get_visitas(self):
        try:
            connection = get_connection()
            visitas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, especialidad, doctor, lugar, fecha, hora  FROM visitamedica ORDER BY fecha ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    visitaMedica = VisitaMedica(row[0], row[1], row[2], row[3], row[4], row[5])
                    visitas.append(visitaMedica.to_JSON())

            connection.close()
            return visitas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_visita(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, especialidad, doctor, lugar, fecha, hora  FROM visitamedica WHERE id = %s", (id,))
                row = cursor.fetchone()

                visitaMedica = None
                if row != None:
                    visitaMedica = VisitaMedica(row[0], row[1], row[2], row[3], row[4], row[5])
                    visitaMedica = visitaMedica.to_JSON()

            connection.close()
            return visitaMedica
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_visita(self, visita):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO visitamedica ( especialidad, doctor, lugar, fecha, hora) 
                                VALUES ( %s, %s, %s, %s, %s)""", ( visita.especialidad, visita.doctor, visita.lugar, visita.fecha, visita.hora))
                affected_rows = cursor.rowcount
                
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_visita(self, visita):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE visitamedica SET especialidad = %s, doctor = %s, lugar = %s, fecha = %s, hora = %s 
                                WHERE id = %s""", (visita.especialidad, visita.doctor, visita.lugar, visita.fecha, visita.hora, visita.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_visita(self, visita):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM visitamedica WHERE id = %s", (visita.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
