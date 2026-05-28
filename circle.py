import shape
import logger
from math import pi

class Circle(shape.Shape):
    """
    class circle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, radius, logger): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        radius(int/float): the radius of the circle
        logger(logging): the logger
       """
       super().__init__(shape_id, shape_type, logger) 
       self.logger.info(f"sent shape_id: {shape_id}, shape_type: {shape_type}, logger to super() in base class")

       if not isinstance(radius, (int, float)):
          self.logger.error(f"type of {radius} should be int/float and not {type(radius)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {radius} should be int/float and not {type(radius)}")
       self.radius = radius

       self.logger.info(f"finished in init in {self.shape_type}. shape_id: {self.shape_id}")
 
    def get_area(self):
       """
       calculate area of circle

       Returns:
        int/float: area of the circle
       """
       self.logger.info(f"in function get_area to get area of {self.shape_type}. shape_id: {self.shape_id}")
       return self.radius * self.radius * pi 
 
    def get_perimeter(self):
       """
       calculate perimeter of circle

       Returns:
            int/float: the circle
       """
       self.logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}. shape_id: {self.shape_id}")
       return 2 * pi * self.radius 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.logger.info(f"in function to_dict to get dict of {self.shape_type}. shape_id: {self.shape_id}")
       return {'id':self.shape_id, 'type':self.shape_type, 'radius':self.radius}
 

   
def main():
    my_logger = logger.get_logger("circle_logger")
    c = Circle(1, "circle", 2, my_logger)
    print(c.get_area())
    print(c.get_perimeter())
    print(c.to_dict())

if __name__ == "__main__":
   main()