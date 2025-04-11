from typing import List

import models
import schemas
from database import engine, session
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.future import select

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def shutdup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipes/', response_model=schemas.BookOut)
async def cook_books(resept: schemas.BookIn) -> models.CookingBook:
    new_resept = models.CookingBook(**resept.dict())
    async with session.begin():
        session.add(new_resept)
    return new_resept


@app.get('/recipes/{recipe_id}', response_model=schemas.BookOut)
async  def one_book(request: Request, recipe_id: int) -> models.CookingBook:
    res = await session.execute(select(models.CookingBook).where(models.CookingBook.id == recipe_id))
    result = res.scalars().one()
    result.count += 1
    await session.commit()
    return templates.TemplateResponse(name="detailed_information.html", context={"request": request, 'cook_book':result})


@app.get('/recipes/', response_model=List[schemas.BookOut])
async def all_books(request: Request) -> List[models.CookingBook]:
    res = await session.execute(select(models.CookingBook))
    cook_books = res.scalars().all()
    return templates.TemplateResponse(name="index.html", context={"request":request, 'cook_books':cook_books})
    #return res.scalars().all()
