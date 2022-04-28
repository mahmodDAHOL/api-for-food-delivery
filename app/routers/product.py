from fastapi import FastAPI, Response, status,Request, HTTPException, Depends, APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import secrets
from sqlalchemy import func
from PIL import Image
from .. import models, schemas, oauth2
from ..database import get_db
import os


router = APIRouter(
    prefix="/products",
    tags=['Products']
)


@router.get("", response_model=List[schemas.ProductOut])
def get_products(db: Session = Depends(get_db)):

    products = db.query(models.Product).all()
    return products


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductOut)
async def create_products(product: schemas.ProductCreate,db: Session = Depends(get_db)):

    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):

    product_query = db.query(models.Product).filter(models.Product.id == id)

    product = product_query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with id: {id} does not exist")


    product_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/uploadfile")
async def create_upload_file(request: Request, file:UploadFile = File(...)):
    FILEPATH = "/app/static/images/"
    filename = file.filename
    extension = filename.split(".")[1]

    if extension not in ["jpg", "png"]:
        return {"status": "error", "detail": "file extension not allowed"}

    # token_name = f"{secrets.token_hex(10)}-{filename}"
    generated_name = FILEPATH+filename
    file_content = await file.read()

    with open(generated_name, "wb") as file:
        file.write(file_content)

    img = Image.open(generated_name)
    img = img.resize(size=(200,200))
    print(generated_name)
    img.save(generated_name)

    file.close()
    # file_url = request.url._url + generated_name
    return {"status": "ok"}

@router.get("/images/{image}")
async def get_image(image:str):
    img_path = f"/app/static/images/{image}"
    return FileResponse(img_path)

@router.get("/images")
async def get_images():
    imgs_path = "/app/static/images"
    images = os.listdir(imgs_path)
    return {"images": images}