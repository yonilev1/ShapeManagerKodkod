import logger
import square, rectangle, circle

class ShapeManager: 
   def __init__(self): 
       self.shapes = [] 
       self.load_from_json()
       self.my_logger = logger.get_logger("shape_logger")

 
   def create_shape(self, shape):
       shape_id = len(self.shapes) + 1
       if shape == 'square':
           length = input("Enter the lentgh of the square side: ")
           my_shape = square.Square(shape_id, shape, length, self.my_logger)
       elif shape == 'rectangle':
           length = input("Enter the lentgh of the rectangle side: ")
           width = input("Enter the width of the rectangle side: ")
           my_shape = rectangle.Rectangle(shape_id, shape, length, width, self.my_logger)
       elif shape == 'circle':
           radius = input("Enter the radius of the circle : ")
           my_shape = square.Square(shape_id, shape, radius, self.my_logger)
        
       self.shapes.append(my_shape)
       self.save_to_json()
            
 
   def get_all_shapes(self): 
       for shape in  
 
   def update_shape(self, shape_id, new_data): 
       pass 
 
   def delete_shape(self, shape_id): 
       pass 
 
   def save_to_json(self): 
       pass 
 
   def load_from_json(self): 
       pass