from database.db import get_connection
from .entities.Treatment import Treatment

class TreatmentModel():
  
  @classmethod
  def get_treatments(self):
    try:
      connection = get_connection
      treatments = []
      
      with connection.cursor() as cursor:
        cursor.execute("SELECT id, pirula_name, start_date, end_date, frecuency, first_dose, last_dose FROM treatment ORDER BY start_date ASC")
        resultset = cursor.fetchall()

        for row in resultset:
          treatment = Treatment(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
          treatments.append(treatment.to_JSON())
      
      connection.close()
      return treatments
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def get_treatment(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, pirula_name, start_date, end_date, frecuency, first_dose, last_dose FROM treatment WHERE id = %s", (id,))
                row = cursor.fetchone()

                treatment = None
                if row != None:
                    treatment = Treatment(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    treatment = Treatment.to_JSON()

            connection.close()
            return treatment
        except Exception as ex:
            raise Exception(ex)

  @classmethod
  def add_treatment(self, treatment):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO treatment (pirula_name, start_date, end_date, frecuency, first_dose, last_dose) 
                                VALUES ( %s, %s, %s, %s, %s, %s)""", ( treatment.pirula_name, treatment.start_date, treatment.end_date, treatment.frecuency, treatment.first_dose, treatment.last_dose))
                affected_rows = cursor.rowcount
                
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

  @classmethod
  def update_treatment(self, treatment):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE treatment SET pirula_name = %s, start_date = %s, end_date = %s, frecuency = %s, first_dose = %s, last_dose = %s 
                                WHERE id = %s""", (treatment.pirula_name, treatment.start_date, treatment.end_date, treatment.frecuency, treatment.first_dose, treatment.last_dose))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

  @classmethod
  def delete_treatment(self, treatment):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM treatment WHERE id = %s", (treatment.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
