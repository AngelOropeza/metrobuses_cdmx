from sqlalchemy.orm import Session

def get_available_units(db: Session):
    return db.execute("""
        SELECT vehicle_id 
        FROM metrobuses
        WHERE vehicle_current_status = '1';
    """).fetchall()

def get_location_by_id(db: Session, unit_id: int):
    return db.execute(f"""
        SELECT position_latitude, position_longitude 
        FROM metrobuses
        WHERE vehicle_id = {unit_id};
    """).fetchone()

def get_mayors(db: Session):
    return db.execute("""
        SELECT DISTINCT alcaldia
        FROM metrobuses
        WHERE vehicle_current_status = '1'
        AND alcaldia IS NOT NULL;
    """).fetchall()

def get_units_by_mayor(db: Session, mayor: str):
    return db.execute(f"""
        SELECT vehicle_id
        FROM metrobuses
        WHERE UNACCENT(alcaldia) ILIKE UNACCENT('%{mayor}%');
    """).fetchall()
