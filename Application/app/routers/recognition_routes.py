from ..controllers.recognition_controllers import FaceRecognitionController

from fastapi import APIRouter

router = APIRouter()

@router.get("/check", tags=["Info"])
async def check_health():
    return await FaceRecognitionController.check_health()

# ------- USE DATABASE INSTEAD -------

@router.get("/person", tags=["Info"])
async def get_all_person():
    return await FaceRecognitionController.get_all_person()

@router.get("/person/{name}", tags=["Info"])
async def get_person(name: str):
    return await FaceRecognitionController.get_person(name)

# @router.put("/person", tags=["Process"])
# async def add_image


# @router.post("/person/compare", tags=["Prcoess"])