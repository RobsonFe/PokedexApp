import models
import schemas
from sqlalchemy.orm import Session


def get_pokemon(db: Session, skip: int = 0, limit: int = 10) -> object:
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(name=pokemon.name, url=pokemon.url)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon
