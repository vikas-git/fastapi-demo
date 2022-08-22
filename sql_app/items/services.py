from sqlalchemy.orm import Session
from . import models, schemas



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    stmt = db.query(models.Item).filter(models.Item.id==item_id)
    if stmt.first():
        stmt.delete(synchronize_session=False)
        db.commit()
        return {"message": "Item Deleted sucessfully !!!"}
    else:
        return {"message": "Item not found !!!"}
