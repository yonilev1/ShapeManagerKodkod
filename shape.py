import logger
class Shape:
   """
   base class for shapes to inharite from
   """
   def __init__(self, shape_id, shape_type, logger):
       """
       constructor

       Args:
            shape_id(int): id of shape
            shape_type(str): type of shape
            looger(logging): logger for the system
       """
       if not logger:
           raise ValueError("the logger cant be None")
       self.logger = logger

       logger.info(f"in super constuctor to init:  shape_id: {shape_id}, shape_type: {shape_type}, logger")

       if not isinstance(shape_id, int):
           self.logger.error(f"type of {shape_id} should be int and not {type(shape_id)}")
           raise ValueError(f"type of {shape_id} should be int and not {type(shape_id)}")
       self.shape_id = shape_id 

       if not isinstance(shape_type, str):
           self.logger.error(f"type of {shape_type} should be str and not {type(shape_type)}")
           raise ValueError(f"type of {shape_type} should be str and not {type(shape_type)}")
       self.shape_type = shape_type 

       self.logger.info("finished in super init")
 
   def get_area(self): 
       pass 
 
   def get_perimeter(self): 
       pass 
 
   def to_dict(self): 
       pass 
   

def main():
    my_logger = logger.get_logger("shape_logger")
    s = Shape(1, "shape", my_logger)
    print(s.get_area())
    print(s.get_perimeter())
    print(s.to_dict())


if __name__ == "__main__":
   main()