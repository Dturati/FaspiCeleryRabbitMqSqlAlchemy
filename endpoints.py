"""Endpoints module."""

from typing import Optional, List

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from services.people_service import PeopleService
from containers import Container
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import People
from models.schema import PeopleSchema
People.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@router.post("/items")
@inject
async def create_item(
  item: PeopleSchema,
  people_service: PeopleService = Depends(Provide[Container.people_service]),
  # db: Session = Depends(get_db)
):
    try:
        res = await people_service.save(item.dict())
        return res
    except Exception as error:
        return str(error)

@router.get("/items")
async def root():
  return {"year": "Hello World"}