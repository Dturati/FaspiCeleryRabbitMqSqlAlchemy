from pydantic import BaseModel

class PeopleSchema(BaseModel):
    name: str
    year: int
    weight: str

    class Config:
        orm_mode = True
