# 1. Library imports
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import tensorflow as tf
import os
from pathlib import Path


class extract_data(BaseModel):
    strings: List[str]

class search_data(BaseModel):
    strings: List[str]
# 2. Create the app objectexit()
app = FastAPI()
model_directory = str(Path(__file__).resolve().parents[1]) + '/Models/'
print(model_directory)
# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.post('/extract/')
async def extract(item: extract_data):
    return extract_data

# @app.post('/search/')
# async def extract(item: extract_data):
#     return extract_data

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
# @app.post('/search/')
# def search(name: str):
#     return {'message': f'Hello, {name}'}

# # 5. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
#load the latest model
    model_list = os.listdir(model_directory)
    model_version = None
    for model_name in model_list:
        if model_name.isnumeric():
            if model_version is None:
                model_version = int(model_name)
                model_path = model_name
            else:
                if int(model_name) < model_version:
                    model_version = int(model_name)
                    model_path = model_name
    assert model_version is not None
    model_path = model_directory + model_path
    model = tf.keras.models.load_model(model_path,compile=False)


    uvicorn.run(app, host='127.0.0.1', port=8000)