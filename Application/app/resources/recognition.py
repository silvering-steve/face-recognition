import os
from typing import Any

import numpy as np
import face_recognition

class FaceRecognition:
    def __init__(self) -> None:
        self.person_data = []
        self.person_encoding_data = []

        self.__prepare_data()

    async def __call__(self, images: np.array, *args: Any, **kwds: Any) -> Any:
        locations = face_recognition.face_locations(images)
        encoding = face_recognition.face_encodings(images, locations)[0]
        distances = face_recognition.face_distance(self.person_encoding_data, encoding)

        match = np.argmin(distances)    

        return self.person_data[match]   

    # ------- USE DATABASE INSTEAD -------
        
    def __prepare_data(self):
        path = ["Application/temp/" + person for person in os.listdir("Application/temp")]

        self.person_data, self.person_encoding_data = (
            [self.__prepare_image(image)[0] for image in path],
            [self.__prepare_image(image)[1] for image in path],
        )

    def __prepare_image(self, path: str):
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]

        name = path.split('/')[-1].replace(".jpeg", "")

        return name, encoding
         
    def add_data(self):
        pass

    def delete_data(self):
        pass


# known_image = face_recognition.load_image_file("Application/images/faces/jovan2.jpeg")
# known_encoding = face_recognition.face_encodings(known_image)[0]

# unknown_image = face_recognition.load_image_file("Application/images/test/vincent2.jpeg")
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# results = face_recognition.face_distance([known_encoding], unknown_encoding)
# print(f"Apakah ini jovan ? {results < .55} dengan total jarak {results}")