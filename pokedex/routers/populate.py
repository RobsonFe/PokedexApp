import httpx
import asyncio
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

router = APIRouter()


async def fetch_pokemon_data(client, url):
    response = await client.get(url)
    response.raise_for_status()
    return response.json()


async def populate_pokemon_db(db: Session) -> object:
    async with httpx.AsyncClient() as client:
        urls = [f"https://pokeapi.co/api/v2/pokemon/{i}" for i in range(1, 151)]
        tasks = []

        async def fetch_and_store(url):
            data = await fetch_pokemon_data(client, url)
            pokemon = schemas.PokemonCreate(name=data["name"], url=url)
            crud.create_pokemon(db, pokemon)

        tasks = [fetch_and_store(url) for url in urls]
        await asyncio.gather(*tasks)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.on_event("startup")
async def startup_event():
    db = next(get_db())
    await populate_pokemon_db(db)
