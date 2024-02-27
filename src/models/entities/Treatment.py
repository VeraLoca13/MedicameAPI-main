from utils.DateFormat import DateFormat

class Treatment():
  def __init__(self, id, pirula_name = None, start_date = None, end_date = None, frecuency = None, first_dose = None, last_dose = None) -> None:
    
    self.id = id
    self.pirula_name = pirula_name
    self.start_date = start_date
    self.end_date = end_date
    self.frecuency = frecuency
    self.first_dose = first_dose
    self.last_dose = last_dose
  
  def to_JSON(self):
    return {
      'id': self.id,
      'pirula_name': self.pirula_name,
      'start_date': self.start_date,
      'end_date': self.end_date,
      'frecuency': self.frecuency,
      'first_dose': self.first_dose,
      'last_dose': self.last_dose
    }