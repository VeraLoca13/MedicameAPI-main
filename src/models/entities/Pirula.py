from utils.DateFormat import DateFormat


class Pirula():

    def __init__(self,id, name = None, brand=None, dose=None,  type=None, amountPerBox=None, withFood=None, withoutFood=None, withOtherPirula=None, currentQuantity=None,) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.dose = dose
        self.type = type
        self.amountPerBox = amountPerBox
        self.withFood = withFood
        self.withoutFood = withoutFood
        self.withOtherPirula = withOtherPirula
        self.currentQuantity = currentQuantity
        
    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'dose': self.dose,
            'type': self.type,
            'amountPerBox': self.amountPerBox,
            'withFood': self.withFood,
            'withoutFood': self.withoutFood,
            'withOtherPirula': self.withOtherPirula,
            'currentQuantity': self.currentQuantity,
        }
