from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_pokemon():
    response = client.post(
        "/pokemon/",
        json={"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "bulbasaur"
