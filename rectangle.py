import shape
import logger

class Rectangle(shape.Shape):
    """
    class rectangle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, length, width, logger): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        length(int/float): the length of 2 Sides
        width(int/float): the width of 2 sides
        logger(logging): the logger
       """
       super().__init__(shape_id, shape_type, logger) 
       self.logger.info(f"sent shape_id: {shape_id}, shape_type: {shape_type}, logger to super() in base class")

       if not isinstance(length, (int, float)):
          self.logger.error(f"type of {length} should be int/float and not {type(length)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {length} should be int/float and not {type(length)}")
       self.length = length

       if not isinstance(width, (int, float)):
          self.logger.error(f"type of {width} should be int/float and not {type(width)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {width} should be int/float and not {type(width)}")
       self.width = width

       self.logger.info(f"finished in init in {self.shape_type}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
 
    def get_area(self):
       """
       calculate area of Rectangle

       Returns:
        int/float: area of the Rectangle
       """
       self.logger.info(f"in function get_area to get area of {self.shape_type}. shape_id: {self.shape_id}")
       return self.length * self.width
 
    def get_perimeter(self):
       """
       calculate perimeter of Rectangle

       Returns:
            int/float: the perimeter
       """
       self.logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}. shape_id: {self.shape_id}")
       return 2 * self.length + 2 * self.width
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.logger.info(f"in function to_dict to get dict of {self.shape_type}. shape_id: {self.shape_id}")
       return {'id':self.shape_id, 'type':self.shape_type, 'side_length':self.length, 'side_width':self.width}


def main():
    my_logger = logger.get_logger("rectangle_logger")
    r = Rectangle(1, "rectangle", 2, 4, my_logger)
    print(r.get_area())
    print(r.get_perimeter())
    print(r.to_dict())


if __name__ == "__main__":
   main()