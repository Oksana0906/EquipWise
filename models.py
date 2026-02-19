"""
Модуль для роботи з даними в базі даних (CRUD операції)
"""

from sqlalchemy.orm import Session
from models import Equipment
from schemas import EquipmentCreate


def get_equipment(db: Session, skip: int = 0, limit: int = 100):
    """Отримати список обладнання"""
    return db.query(Equipment).offset(skip).limit(limit).all()


def get_equipment_by_id(db: Session, equipment_id: int):
    """Отримати обладнання за ID"""
    return db.query(Equipment).filter(Equipment.id == equipment_id).first()


def create_equipment(db: Session, equipment: EquipmentCreate):
    """Створити нове обладнання"""
    db_equipment = Equipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def seed_database(db: Session):
    """Заповнити базу даних тестовими даними"""
    # Перевірка, чи таблиця порожня
    if db.query(Equipment).first() is None:
        # Створення тестових записів (4 комп'ютери)
        test_equipment = [
            Equipment(
                name="Комп'ютер Dell OptiPlex",
                type="Комп'ютер",
                department="IT-відділ",
                max_capacity=100.0,
                current_load=85.0,
                purchase_cost=800.0,
                lifetime_years=4,
                status="Активний"
            ),
            Equipment(
                name="Комп'ютер Lenovo ThinkCentre",
                type="Комп'ютер",
                department="Маркетинг",
                max_capacity=100.0,
                current_load=45.0,
                purchase_cost=750.0,
                lifetime_years=4,
                status="Активний"
            ),
            Equipment(
                name="Комп'ютер HP EliteDesk",
                type="Комп'ютер",
                department="Фінанси",
                max_capacity=100.0,
                current_load=25.0,
                purchase_cost=700.0,
                lifetime_years=4,
                status="Активний"
            ),
            Equipment(
                name="Комп'ютер ASUS VivoMini",
                type="Комп'ютер",
                department="Відділ продажів",
                max_capacity=100.0,
                current_load=95.0,
                purchase_cost=650.0,
                lifetime_years=4,
                status="Активний"
            )
        ]
        
        # Додавання тестових записів
        db.add_all(test_equipment)
        db.commit()