from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


from sql_app.items import schemas, services as crud
from sql_app.database import get_db

router = APIRouter(tags=["Items"])


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.delete("/items/{item_id}/")
def create_item_for_user(item_id: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=404, content={"message": "Item not found"})
    # return crud.delete_item(db=db, item_id=item_id)
