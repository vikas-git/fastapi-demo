from fastapi import Depends, FastAPI
from sql_app.items.item_router import router as item_router
from sql_app.users.user_router import router as user_router

from sql_app.users import models as user_models
from sql_app.items import models as item_models

# apply migration
from sql_app.database import engine
for model in [user_models, item_models]:
    model.Base.metadata.create_all(bind=engine)


# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(user_router, prefix="/api")
app.include_router(item_router, prefix="/api/v1")
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app)