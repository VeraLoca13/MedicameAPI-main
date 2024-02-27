from database.db import get_connection
from .entities.Treatment import Treatment

class TreatmentModel():
  
  @classmethod
  def get_treatments(self):
    try:
      connection = get_connection
      treatments = []
      
      with connection.cursor() as cursor:
        cursor.execute("SELECT id, ")