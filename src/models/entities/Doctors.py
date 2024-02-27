
class Doctor():
  
  def __init__(self, id, medicalSpeciality = None, name = None, ocupation = None, age = None, shift = None) -> None:
    self.id = id
    self.medicalSpeciality = medicalSpeciality
    self.name = name
    self.ocupation = ocupation
    self.age = age
    self.shift = shift
  
  def to_JSON(self):
    return {
      'id': self.id,
      'medicalSpeciality': self.medicalSpeciality,
      'name': self.name,
      'ocupation': self.ocupation,
      'age': self.age,
      'shift': self.shift
    }