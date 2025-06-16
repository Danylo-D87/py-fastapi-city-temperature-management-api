from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies import get_db
from schemas import city
from crud import city as crud


router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


@router.get("/", response_model=List[city.CityReadSchema], summary="Get all cities")
async def get_all_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_cities(db)


@router.post(
    "/",
    response_model=city.CityReadSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new city",
)
async def create_city(
        city_data: city.CityCreateSchema,
        db: AsyncSession = Depends(get_db)
):
    return await crud.create_city(db, city_data)


@router.delete(
    "/{city_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a city by ID",
)
async def delete_city(
        city_id: int,
        db: AsyncSession = Depends(get_db)
):
    await crud.delete_city(db, city_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
