from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/pokemon/", response_model=List[schemas.Pokemon])
def read_pokemon(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pokemons = crud.get_pokemon(db, skip=skip, limit=limit)
    return pokemons


@router.post("/pokemon/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)):
    return crud.create_pokemon(db, pokemon)
