import logger
import square, rectangle, circle
import json

class ShapeManager: 
   def __init__(self): 
       self.my_logger = logger.get_logger("shape_logger")
       self.shapes = [] 
       self.load_from_json()
       self.my_logger.info("in init of ShapeManager")
       


   def create_shape(self, shape):
       """
       create shape by users demand

       Args:
        shape(str): the shape user wants
       """
       self.my_logger.info(f"in shape manager. in create shape with shape {shape}")

       shape_id = len(self.shapes) + 1
       if not isinstance(shape, str):
           self.my_logger.error(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
           raise ValueError(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
       
       if shape == 'square':
           self.my_logger.info("the shape wanted is square, sending to create in instans")
           length = input("Enter the lentgh of the square side: ")
           my_shape = square.Square(shape_id, shape, length, self.my_logger)
       elif shape == 'rectangle':
           self.my_logger.info("the shape wanted is rectangle, sending to create in instans")
           length = input("Enter the lentgh of the rectangle side: ")
           width = input("Enter the width of the rectangle side: ")
           my_shape = rectangle.Rectangle(shape_id, shape, length, width, self.my_logger)
       elif shape == 'circle':
           self.my_logger.info("the shape wanted is circle, sending to create in instans")
           radius = input("Enter the radius of the circle : ")
           my_shape = circle.Circle(shape_id, shape, radius, self.my_logger)
        
       else:
           self.my_logger.error("got wrong shape type, can get only - circle, square, rectangle")
           raise ValueError("got wrong shape type, can get only - circle, square, rectangle")
           
        
       self.shapes.append(my_shape)
       self.save_to_json()
       self.my_logger.info("shape created successfully, updated json")
            
 
   def get_all_shapes(self):
       """
       print all shapes in this way
       """
       self.my_logger("in shape manager. in get all shapes to print all shapes")
       for shape in self.shapes:
           if shape['type'] == 'circle':
               print(f'ID: {shape['id']} \n Type: {shape['type']} \n Radius: {shape['radius']} \n Area: {shape.area()} \n Perimeter: {shape.perimeter()}')
           elif shape['type'] == 'square':
               print(f'ID: {shape['id']} \n Type: {shape['type']} \n Side: {shape['length']} \n Area: {shape.area()} \n Perimeter: {shape.perimeter()}')
           elif shape['type'] == 'rectangle':
               print(f'ID: {shape['id']} \n Type: {shape['type']} \n Side_len: {shape['length']} \n  Side_wid: {shape['width']} \n Area: {shape.area()} \n Perimeter: {shape.perimeter()}')
            
         


   def update_shape(self, shape_id, new_data): 
       """
       to update a shapes size

       Args:
        shape_id(int): ths uid of shape
        new_date(int/float): new data to update
       """
       self.my_logger.info("in shape manager. trying to update the shape")
       
       if not isinstance(shape_id, (int,float)):
           self.my_logger.error(f"shape id not valid, can get only int or float and got {type(shape_id)}")
           raise ValueError(f"shape id not valid, can get only int or float and got {type(shape_id)}")
       
       if not isinstance(new_data, (int,float)):
           self.my_logger.error(f"new_data not valid, can get only int or float and got {type(new_data)}")
           raise ValueError(f"new_data not valid, can get only int or float and got {type(new_data)}")
       
       for shape in self.shapes:
           if shape['id'] == shape_id:
               if shape['type'] == 'circle':
                   self.my_logger.info("shape is circle, updating radius")
                   shape['radius'] = new_data
                   self.save_to_json()
                   return
               elif shape['type'] == 'square':
                   self.my_logger.info("shape is square, updating length")
                   shape['length'] = new_data
                   self.save_to_json()
                   return
               elif shape['type'] == 'rectangle':
                   side = input("length or width: ")
                   self.my_logger.info(f"shape is rectangle, updating {side.lower()}")
                   shape[side.lower()] = new_data
                   self.save_to_json()
                   return
       self.my_logger.warning("didnt find shape id in the DB, didnt update.")

 
   def delete_shape(self, shape_id):
       """
       to delete shape from list

       Args:
            shape_id(int): id of shape
       """
       self.my_logger.info("in shape manager. trying to delete shape by id")
       for shape in self.shapes:
           if shape['id'] == shape_id:
               self.shapes.remove(shape)
               self.save_to_json()
               return
       self.my_logger.warning("didnt find shape id in the DB, didnt delete.")

 
   def save_to_json(self):
       """
       function to save the shapes and changes to json
       """
       self.my_logger.info("in shape manager. trying to save the shapes and changes to json")
       try:
            with open('shapes.json', 'w', encoding='utf-8') as json_file:
                json.dump(self.shapes, json_file, indent=4)
       except FileNotFoundError as e:
           self.my_logger.exception(f"there was an exeption while opening the json: {e}")
           

 
   def load_from_json(self): 
       """
       function to load the shapes from json
       """
       self.my_logger.info("in shape manager. trying to load the shapes from json")
       try:
            with open('shapes.json', 'r', encoding='utf-8') as json_file:
                json.load(self.shapes, json_file)
       except FileNotFoundError as e:
           self.my_logger.exception(f"there was an exeption while opening the json: {e}")
           