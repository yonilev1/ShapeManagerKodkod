import logger
import square, rectangle, circle
import json

class ShapeManager:
   """
   class shapemanager to manage all operations related to the shapes
   """
   def __init__(self):
       """
       init function
       """
       self.my_logger = logger.get_logger("shape_logger")
       self.shapes = [] 
       self.load_from_json()
       self.my_logger.info("in init of ShapeManager")
       


   def create_shape(self, shape, length=None, width=None, radius=None):
       """
       create shape by users demand

       Args:
        shape(str): the shape user wants
       """
       shape_id = len(self.shapes) + 1
       self.my_logger.info(f"in shape manager. in create shape with shape: {shape}, id: {shape_id}")

       if not isinstance(shape, str):
           self.my_logger.error(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
           raise ValueError(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
       
       if shape == 'square':
           self.my_logger.info("the shape wanted is square, sending to create in instans")
           my_shape = square.Square(shape_id, shape, length, self.my_logger)
       elif shape == 'rectangle':
           self.my_logger.info("the shape wanted is rectangle, sending to create in instans")
           my_shape = rectangle.Rectangle(shape_id, shape, length, width, self.my_logger)
       elif shape == 'circle':
           self.my_logger.info("the shape wanted is circle, sending to create in instans")
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
       self.my_logger.info(f"in shape manager. in get all shapes to print all shapes. len of shapes: {len(self.shapes)}")
       for shape in self.shapes:
           if isinstance(shape, circle.Circle):
               print(f'ID: {shape.shape_id} \n Type: {shape.shape_type} \n Radius: {shape.radius} \n Area: {shape.get_area()} \n Perimeter: {shape.get_perimeter()}')
           elif isinstance(shape, square.Square):
               print(f'ID: {shape.shape_id} \n Type: {shape.shape_type} \n Side: {shape.length} \n Area: {shape.get_area()} \n Perimeter: {shape.get_perimeter()}')
           elif isinstance(shape, rectangle.Rectangle):
               print(f'ID: {shape.shape_id} \n Type: {shape.shape_type} \n Side_len: {shape.length} \n  Side_wid: {shape.width} \n Area: {shape.get_area()} \n Perimeter: {shape.get_perimeter()}')
            
         


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
       list_to_save_to_json = []
       try:
            with open('shapes.json', 'w', encoding='utf-8') as json_file:
                for shape in self.shapes:
                    list_to_save_to_json.append(shape.to_dict())
                json.dump(list_to_save_to_json, json_file, indent=4)
       except FileNotFoundError as e:
           self.my_logger.exception(f"there was an exeption while opening the json: {e}")
           

 
   def load_from_json(self): 
       """
       function to load the shapes from json
       """
       self.my_logger.info("in shape manager. trying to load the shapes from json")
       #links_to_classes = {'circle':circle.Circle, 'square':square.Square, 'rectangle':rectangle.Rectangle} 
       try:
            with open('shapes.json', 'r', encoding='utf-8') as json_file:
                try:
                    temp_shapes = json.load(json_file)
                    self.my_logger.info(f"extract json to temp list, there are {len(temp_shapes)} shapes")
                    for item in temp_shapes:
                        self.my_logger.info(f"trying to turn shape {item} back in to object style")
                        if item['type'] == 'circle':
                            self.shapes.append(circle.Circle(item['id'], item['type'], item['radius'], self.my_logger))
                        elif item['type'] == 'square':
                            self.shapes.append(square.Square(item['id'], item['type'], item['side'], self.my_logger))
                        elif item['type'] == 'rectandle':
                            self.shapes.append(rectangle.Rectangle(item['id'], item['type'], item['side_length'], item['side_width'], self.my_logger))
                except Exception as e:
                    self.my_logger.exception(f"there was an exeption while reading the json: {e}")

       except FileNotFoundError as e:
           self.my_logger.exception(f"there was an exeption while opening the json: {e}")


def main():
    sm = ShapeManager()
    sm.create_shape('square')
    sm.get_all_shapes()

    sm.create_shape('circle')
    sm.get_all_shapes()

    sm.create_shape('rectangle')
    sm.get_all_shapes()




if __name__ == "__main__":
    main()
           