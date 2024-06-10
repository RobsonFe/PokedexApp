import uvicorn
from fastapi import FastAPI

import models
from database import engine
from routers import pokemon, populate

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(pokemon.router)
app.include_router(populate.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
