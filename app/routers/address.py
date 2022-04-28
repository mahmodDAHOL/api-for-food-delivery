from urllib.parse import urlencode

import requests
from app.config import settings
from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Response,
                     status)
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/address",
    tags=['Address']
)


@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_address(address: schemas.Address, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_address = models.Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


@router.get("/list")
def get_addresses(address: Address, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    addresses = db.query(models.Address).filter(
        models.Address.contactPersonName == current_user.name).all()

    return addresses


@router.post("/geocode-api")
def get_address_info(latlng: schemas.AddressCordinates, db: Session = Depends(get_db)):

    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
    latlng = f'{latlng.latitude},{latlng.longitude}'
    params = {"latlng": latlng, "key": settings.google_map_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    return r
