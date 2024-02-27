from utils.DateFormat import DateFormat


class Pirula():

    def __init__(self,id, name = None, brand=None, dose=None,  type=None, amount_per_box=None, with_food=None, without_food=None, with_other_pirula=None, current_quantity=None,) -> None:
        self.id = id
        self.name = name
        self.brand = brand
        self.dose = dose
        self.type = type
        self.amount_per_box = amount_per_box
        self.with_food = with_food
        self.without_food = without_food
        self.with_other_pirula = with_other_pirula
        self.current_quantity = current_quantity
        
    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'dose': self.dose,
            'type': self.type,
            'amountPerBox': self.amount_per_box,
            'withFood': self.with_food,
            'withoutFood': self.without_food,
            'withOtherPirula': self.with_other_pirula,
            'currentQuantity': self.current_quantity,
        }
