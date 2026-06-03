from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
import shape_manager


router = APIRouter()


class CreateShape(BaseModel):
    """Request body for creating a new shape."""
    shape_type : str
    length_radius : int
    width : int | None = None

class UpdateShape(BaseModel):
    """Request body for updating an existing shape's dimensions."""
    length_or_radius : int
    width : int | None = None


def get_shape_manager():
    return shape_manager.ShapeManager()


@router.post('/shapes', status_code=status.HTTP_201_CREATED)
def create_shape(shape : CreateShape, sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Create a new shape and return its generated ID."""
    try:
        created_shape = sm.create_shape(shape.shape_type, shape.length_radius, shape.width)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    return {'shape id': created_shape}


@router.get('/shapes/')
def get_all_shapes(sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Return a list of all existing shapes."""
    try:
        return {'message': sm.get_all_shapes()}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")


@router.get('/shapes/total-area')
def get_total_shapes_area(sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Return the sum of areas of all shapes."""
    try:
        return {'message': f'The sum of all area: {sm.get_sum_area()}'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")


@router.get('/shapes/count')
def get_amount_of_shapes(sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Return the total number of shapes."""
    try:
        return {'message': f'there are: {sm.count_shapes()} shapes in total.'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")


@router.get('/shapes/type/{type}')
def get_shapes_by_type(type:str, sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Return all shapes matching the given type."""
    try:
        if type not in ['circle', 'square', 'rectangle']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"wronge shape {type}")
        types = sm.get_shapes_by_type(type)
        return {'message': types}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
    

@router.get('/shapes/{id}')
def get_shape_by_id(id:int, sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Return a single shape by its ID."""
    try:
        return {'message': sm.get_shape_by_id(id)}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")


@router.put('/shapes/{id}')
def update_shape(id:int, update : UpdateShape, sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Update dimensions of a shape by its ID."""
    try:
        did_update = sm.update_shape(id, update.length_or_radius, update.width)
        if did_update:
            return {"message": f'shape {id} updated successfully.'}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"didnt find shape id {id}")
    except Exception as e:
        if str(e) == f"'didnt find the id: {id}'":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"didnt find shape id {id}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")


@router.delete('/shapes/{id}')
def delete_shape_by_id(id:int, sm: shape_manager.ShapeManager = Depends(get_shape_manager)):
    """Delete a shape by its ID."""
    try:
        did_delete = sm.delete_shape(id)
        if did_delete:
            return {'message': 'shape deleted successfuly'}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} was not found")
    except Exception as e:
        print(str(e))
        if str(e) == f"'the key {id} does not exist.'":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} was not found")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")

