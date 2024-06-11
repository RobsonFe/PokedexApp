import uvicorn
import xmltodict
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from schemas import Pokemon
import models
from database import engine
from routers import pokemon, populate
from routers.pokemon import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pokemon.router)
app.include_router(populate.router)


@app.get("/pokemons/xml")
async def get_pokemons_xml(db: Session = Depends(get_db)):
    try:

        pokemons = db.query(Pokemon).order_by(Pokemon.name).all()

        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemons found")

        pokemon_list = [{"id": p.id, "name": p.name} for p in pokemons]

        pokemons_dict = {"pokemons": {"pokemon": pokemon_list}}

        xml_data = xmltodict.unparse(pokemons_dict, pretty=True)

        return Response(content=xml_data, media_type="application/xml")
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
