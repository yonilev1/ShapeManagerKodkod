from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import shape_manager

class CreateShape(BaseModel):
    shape_type : str
    length_radius : int
    width : int | None = None

class UpdateShape(BaseModel):
    length_or_radius : int
    width : int | None = None


app = FastAPI()

@app.post('/shapes', status_code=status.HTTP_201_CREATED)
def create_shape(shape : CreateShape):
    sm = shape_manager.ShapeManager()
    try:
        created_shape = sm.create_shape(shape.shape_type, shape.length_radius, shape.width)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    return {'shape id': created_shape}


@app.get('/shapes/')
def get_all_shapes():
    sm = shape_manager.ShapeManager()
    try:
        return {'message': sm.get_all_shapes()}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
    

@app.get('/shapes/total-area')
def get_total_shapes_area():
    sm = shape_manager.ShapeManager()
    try:
        return {'message': sm.get_sum_area()}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")    
    

@app.get('/shapes/count')
def get_amount_of_shapes():
    sm = shape_manager.ShapeManager()
    return {'message': f'there are: {sm.count_shapes()} shapes in total.'}
    

@app.get('/shapes/{id}')
def get_shape_by_id(id:int):
    sm = shape_manager.ShapeManager()
    try:
        return {'message': sm.get_shape_by_id(id)}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
    

@app.get('/shapes/type/{type}')
def get_shapes_by_type(type:str):
    sm = shape_manager.ShapeManager()
    try:
        types = sm.get_shapes_by_type(type)
        return {'message': types}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    

@app.put('/shapes/{id}')
def update_shape(id:int, update : UpdateShape):
    sm = shape_manager.ShapeManager()
    try:
        did_update = sm.update_shape(id, update.length_or_radius, update.width)
        if did_update:
            return {"message": f'shape {id} updated successfully.'}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"didnt find shape id {id}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    

@app.delete('/shapes/{id}')
def delete_shape_by_id(id:int):
    sm = shape_manager.ShapeManager()
    try:
        did_delete = sm.delete_shape(id)
        if did_delete:
            return {'message': 'shape deleted successfuly'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
