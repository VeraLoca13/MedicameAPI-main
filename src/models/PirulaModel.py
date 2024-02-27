from database.db import get_connection
from .entities.Pirula import Pirula


class PirulaModel():

    @classmethod
    def get_pirulas(self):
        try:
            connection = get_connection()
            pirulas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, brand, dose,  type, amountPerBox, withFood, withoutFood, withOtherPirula, currentQuantity FROM pirula ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    pirula = pirula(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    pirulas.append(pirula.to_JSON())

            connection.close()
            return pirulas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_visita(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, brand, dose,  type, amountPerBox, withFood, withoutFood, withOtherPirula, currentQuantity FROM pirula WHERE id = %s", (id,))
                row = cursor.fetchone()

                pirula = None
                if row != None:
                    pirula = pirula(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    pirula = pirula.to_JSON()

            connection.close()
            return pirula
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_visita(self, pirula):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO pirula (name, brand, dose,  type, amountPerBox, withFood, withoutFood, withOtherPirula, currentQuantity) 
                                VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", ( pirula.name, pirula.brand, pirula.dose, pirula.type, pirula.amountPerBox, pirula.withFood, pirula.withoutFood, pirula.lugar, pirula.withOtherPirula, pirula.currentQuantity))
                affected_rows = cursor.rowcount
                
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_visita(self, pirula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE pirula SET especialidad = %s, doctor = %s, lugar = %s, fecha = %s, hora = %s 
                                WHERE id = %s""", (pirula.name, pirula.brand, pirula.dose, pirula.type, pirula.amountPerBox, pirula.withFood, pirula.withoutFood, pirula.lugar, pirula.withOtherPirula, pirula.currentQuantity, pirula.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_visita(self, pirula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pirula WHERE id = %s", (pirula.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
