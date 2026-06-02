import logger
from square import Square
from rectangle import Rectangle
from circle import Circle
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
       self.contructors = {'circle': Circle, 'square':Square, 'rectangle':Rectangle}
       self.__load_from_json()
       self.my_logger.info("in init of ShapeManager")
       


   def create_shape(self, shape, length_radius=None, width=None):
       """
       create shape by users demand

       Args:
        shape(str): the shape user wants

       Returns:
        int: id of created shape
       """
       shape_id = self.__calculate_id()
       self.my_logger.info(f"in shape manager. in create shape with shape: {shape}, id: {shape_id}")

       if not isinstance(shape, str):
           self.my_logger.error(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
           raise ValueError(f"got wrong shape type {type(shape)}, can get only - str with: circle, square, rectangle")
       
       contructor = self.contructors[shape]
       my_shape = contructor(shape_id, shape, self.my_logger, length_radius, width)
                   
       self.shapes.append(my_shape)
       self.__save_to_json()
       self.my_logger.info(f"shape {shape} with id {shape_id} created successfully, updated json")
       return shape_id
            
 
   def get_all_shapes(self):
       """
       print all shapes in this way
       """
       self.my_logger.info(f"in shape manager. in get all shapes to print all shapes. len of shapes: {len(self.shapes)}")
       for shape in self.shapes:
           print(shape.print_details())
         


   def update_shape(self, shape_id, new_data_1, new_data_2=None): 
       """
       to update a shapes size

       Args:
        shape_id(int): ths uid of shape
        new_date(int/float): new data to update
       """
       self.my_logger.info("in shape manager. trying to update the shape")
       
       if not isinstance(shape_id, int):
           self.my_logger.error(f"shape id not valid, can get only int and got {type(shape_id)}")
           raise ValueError(f"shape id not valid, can get only int and got {type(shape_id)}")
       
       if new_data_1 and not isinstance(new_data_1, int):
           self.my_logger.error(f"new_data not valid, can get only int and got {type(new_data_1)}")
           raise ValueError(f"new_data not valid, can get only int and got {type(new_data_1)}")
       
       if new_data_2 and not isinstance(new_data_2, int):
           self.my_logger.error(f"new_data not valid, can get only int and got {type(new_data_2)}")
           raise ValueError(f"new_data not valid, can get only int and got {type(new_data_2)}")
              
       for shape in self.shapes:
           if shape.shape_id == shape_id:
               shape.update_shape(new_data_1, new_data_2)
               self.__save_to_json()
               self.my_logger.info(f"apdated the shape {shape.shape_type} with id {shape.shape_id}, and save to json")
               return True
       self.my_logger.warning(f"didnt find shape id {shape_id} in the DB, didnt update.")
       raise KeyError(f"the key {shape_id} does not exist.")

 
   def delete_shape(self, shape_id):
       """
       to delete shape from list

       Args:
            shape_id(int): id of shape
       """
       self.my_logger.info("in shape manager. trying to delete shape by id")           
       
       for shape in self.shapes:
           if shape.shape_id == shape_id:
               self.shapes.remove(shape)
               self.__save_to_json()
               self.my_logger.info(f"deleted the shape {shape.shape_type} with id {shape.shape_id}, and save to json")
               return True
       self.my_logger.warning(f"didnt find shape id {shape_id} in the DB, didnt delete.")
       raise KeyError(f"the key {shape_id} does not exist.")

 
   def __save_to_json(self):
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
           

 
   def __load_from_json(self): 
       """
       function to load the shapes from json
       """
       self.my_logger.info("in shape manager. trying to load the shapes from json")
       try:
            with open('shapes.json', 'r', encoding='utf-8') as json_file:
                try:
                    temp_shapes = json.load(json_file)
                    self.my_logger.info(f"extract json to temp list, there are {len(temp_shapes)} shapes")
                    for shape in temp_shapes:
                        contructor = self.contructors[shape['type']]
                        width = None
                        if 'side_width' in shape.keys():
                            width = shape['side_width']
                        shape_back_to_object = contructor(shape['id'], shape['type'], self.my_logger, shape['length/radius'], width)
                        self.shapes.append(shape_back_to_object)
                        self.my_logger.info(f"trying to turn shape {shape['type']} with id {shape['id']} back in to object style")
                except Exception as e:
                    self.my_logger.exception(f"there was an exeption while reading the json: {e}")

       except FileNotFoundError as e:
           self.my_logger.exception(f"there was an exeption while opening the json: {e}")


   def __get_keys(self):
       """
       get all keys of shapes

       Returns:
        List: list of all keys
       """
       if len(self.shapes) == 0:
           return []
       return [shape.shape_id for shape in self.shapes]
       
    
   def __calculate_id(self):
       """
       calculate id based on largest index

       Returns:
            int: id of shape
       """
       if not self.shapes:
           return 1
       return max(self.__get_keys()) + 1
   

   def get_shape_by_id(self, id):
       """
       function to get the kind of shape by its id

       Args:
            id(int): shapes uid
        
        Returns:
            str: the kind of shape
       """
       for shape in self.shapes:
           if shape.shape_id == id:
               self.my_logger.info(f"found the shape by its id: {id}, returning shapes kind")
               return shape.to_dict()
       self.my_logger.warning(f"didnt find the id: {id}")
       raise KeyError(f"didnt find the id: {id}")


def main():
    sm = ShapeManager()
    sm.get_shape_by_id(12)
    """sm.update_shape(8, 1)
    sm.create_shape('square')
    sm.get_all_shapes()

    sm.create_shape('circle')
    sm.get_all_shapes()

    sm.create_shape('rectangle')
    sm.get_all_shapes()"""


if __name__ == "__main__":
    main()
           