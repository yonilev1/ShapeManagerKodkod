import logger
class Shape:
   """
   base class for shapes to inharite from
   """
   def __init__(self, shape_id, shape_type, my_logger):
       """
       constructor

       Args:
            shape_id(int): id of shape
            shape_type(str): type of shape
            looger(logging): my_logger for the system
       """
       if not my_logger:
           raise ValueError("the my_logger cant be None")
       self.my_logger = my_logger

       my_logger.info(f"in super constuctor to init:  shape_id: {shape_id}, shape_type: {shape_type}, my_logger")

       if not isinstance(shape_id, int):
           self.my_logger.error(f"type of {shape_id} should be int and not {type(shape_id)}")
           raise ValueError(f"type of {shape_id} should be int and not {type(shape_id)}")
       self.shape_id = shape_id 

       if not isinstance(shape_type, str):
           self.my_logger.error(f"type of {shape_type} should be str and not {type(shape_type)}")
           raise ValueError(f"type of {shape_type} should be str and not {type(shape_type)}")
       self.shape_type = shape_type 

       self.my_logger.info("finished in super init")
 
   def get_area(self): 
       pass 
 
   def get_perimeter(self): 
       pass 
 
   def to_dict(self): 
       pass 
   
   def print_details(self):
       pass
   
   def update_shape(self, shape, new_size_1, new_size_2=None):
       pass
   

def main():
    my_logger = logger.get_logger("shape_my_logger")
    s = Shape(1, "shape", my_logger)
    print(s.get_area())
    print(s.get_perimeter())
    print(s.to_dict())


if __name__ == "__main__":
   main()