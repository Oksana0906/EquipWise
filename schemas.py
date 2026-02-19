"""
Pydantic схеми для валідації даних
"""

from pydantic import BaseModel


class EquipmentBase(BaseModel):
    """Базова схема обладнання"""
    name: str
    type: str
    department: str
    max_capacity: float
    current_load: float
    purchase_cost: float
    lifetime_years: int
    status: str


class EquipmentCreate(EquipmentBase):
    """Схема для створення обладнання"""
    pass


class Equipment(EquipmentBase):
    """Схема для повернення даних про обладнання"""
    id: int

    class Config:
        from_attributes = True