
class Doctor():
  
  def __init__(self, id, medical_speciality = None, name = None, ocupation = None, age = None, shift = None) -> None:
    self.id = id
    self.medical_speciality = medical_speciality
    self.name = name
    self.ocupation = ocupation
    self.age = age
    self.shift = shift
  
  def to_JSON(self):
    return {
      'id': self.id,
      'medical_speciality': self.medical_speciality,
      'name': self.name,
      'ocupation': self.ocupation,
      'age': self.age,
      'shift': self.shift
    }