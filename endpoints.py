"""Endpoints module."""

from typing import Optional, List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide

from services.people import PeopleService
from containers import Container

router = APIRouter()

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

@router.post("/items")
@inject
async def create_item(
  item: Item,
  people_service: PeopleService = Depends(Provide[Container.people_service])
):
  res = await people_service.save(item.dict())
  return res

@router.get("/items")
async def root():
  return {"year": "Hello World"}