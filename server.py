from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import shape_manager

class Shape(BaseModel):
    shape_type : str
    length_radius : int
    width : int | None


app = FastAPI()

@app.post('/shapes', status_code=status.HTTP_201_CREATED)
def create_shape(shape : Shape):
    sm = shape_manager.ShapeManager()
    try:
        created_shape = sm.create_shape(shape.shape_type, shape.length_radius, shape.width)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    return {'shape id': created_shape}



@app.get('/shapes/{id}')
def get_shape_by_id(id:int):
    sm = shape_manager.ShapeManager()
    try:
        return sm.get_shape_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
    


@app.get('/shapes/')
def get_all_shapes():
    sm = shape_manager.ShapeManager()
    try:
        return sm.get_all_shapes()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
    





