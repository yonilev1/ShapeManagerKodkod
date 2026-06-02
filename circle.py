import shape
import logger
from math import pi

class Circle(shape.Shape):
    """
    class circle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, my_logger, *args): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        radius(int/float): the radius of the circle
        my_logger(logging): the my_logger
       """
       super().__init__(shape_id, shape_type, my_logger) 
       self.my_logger.info(f"sent shape_id: {shape_id}, shape_type: {shape_type}, my_logger to super() in base class")
       if not args:
          raise ValueError("Didnt get sizes, args in empty")
       
       radius = args[0]
       if not isinstance(radius, (int, float)):
          self.my_logger.error(f"type of {radius} should be int/float and not {type(radius)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {radius} should be int/float and not {type(radius)}")
       
       if radius <= 0:
          self.my_logger.error(f"radius should be larger then 0. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"radius should be larger then 0. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
       
       self.radius = radius

       self.my_logger.info(f"finished in init in {self.shape_type}. shape_id: {self.shape_id}")
 
    def get_area(self):
       """
       calculate area of circle

       Returns:
        int/float: area of the circle
       """
       self.my_logger.info(f"in function get_area to get area of {self.shape_type}. shape_id: {self.shape_id}")
       return self.radius * self.radius * pi 
 
    def get_perimeter(self):
       """
       calculate perimeter of circle

       Returns:
            int/float: the circle
       """
       self.my_logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}. shape_id: {self.shape_id}")
       return 2 * pi * self.radius 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.my_logger.info(f"in function to_dict to get dict of {self.shape_type}. shape_id: {self.shape_id}")
       return {'id':self.shape_id, 'type':self.shape_type, 'length/radius':self.radius}
    

    def print_details(self):
       return f"""ID: {self.shape_id}\n
       Type: {self.shape_type}\n
       Radius:{self.radius}\n
       Area: {self.get_area():.2f}\n
       Perimeter: {self.get_perimeter():.2f}\n"""
    

    def update_shape(self, new_size_1, new_size_2=None):
       if new_size_1 is not None:
            self.radius = new_size_1
 

   
def main():
    my_logger = logger.get_logger("circle_my_logger")
    c = Circle(1, "circle", 2, my_logger)
    print(c.get_area())
    print(c.get_perimeter())
    print(c.to_dict())

if __name__ == "__main__":
   main()