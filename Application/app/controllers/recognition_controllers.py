import os


from ..error.exception import (
    DetailedHTTPException, 
    PersonNotFound, 
    DatabaseNotFound
)
from ..resources.recognition import face_recognition

from starlette.responses import JSONResponse, FileResponse

class FaceRecognitionController:
    @staticmethod
    async def check_health() -> JSONResponse:
        try:
            return JSONResponse(
                status_code=200,
                content={
                    "message": "healthy"
                }
            )
        except Exception:
            raise DetailedHTTPException
    
    # ------- USE DATABASE INSTEAD -------

    @staticmethod
    async def get_person(name: str) -> FileResponse:
        path = f"Application/temp/{name}.jpeg"

        if os.path.exists(path):
            return FileResponse(
                status_code=200,
                path=path
            )
        
        raise PersonNotFound

    @staticmethod
    async def get_all_person() -> JSONResponse:

        if os.path.exists("Application/temp"):
            return JSONResponse(
                    status_code=200,
                    content={
                        "person": [x.replace(".jpeg", "") for x in os.listdir("Application/temp")]
                    }
                )

        raise DatabaseNotFound