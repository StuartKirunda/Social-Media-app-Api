
from fastapi import FastAPI


from . import models
from .database import engine
from .routers import post, user, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# route importation


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
# Home


@app.get("/")
def root():
    return {"message": "Welcome to my api!!!!!"}
