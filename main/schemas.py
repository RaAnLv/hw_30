from pydantic import BaseModel


class BaseBook(BaseModel):
    name: str
    product_list: str
    time_cook: str
    description: str


class BookIn(BaseBook): ...


class BookOut(BaseBook):
    id: int
    count: int

    class Config:
        orm_mode = True

