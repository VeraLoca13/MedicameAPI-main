from utils.DateFormat import DateFormat

class Treatment():
  def __init__(self, id, pirulaName = None, startDate = None, endDate = None, frecuency = None, firstDose = None, lastDose = None) -> None:
    
    self.id = id
    self.pirulaName = pirulaName
    self.startDate = startDate
    self.endDate = endDate
    self.frecuency = frecuency
    self.firstDose = firstDose
    self.lastDose = lastDose
  
  def to_JSON(self):
    return {
      'id': self.id,
      'pirulaName': self.pirulaName,
      'startDate': self.startDate,
      'endDate': self.endDate,
      'frecuency': self.frecuency,
      'firstDose': self.firstDose,
      'lastDose': self.lastDose
    }