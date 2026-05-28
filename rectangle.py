import shape
import logger

class Rectangle(shape.Shape):
    """
    class rectangle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, my_logger, *args): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        length(int/float): the length of 2 Sides
        width(int/float): the width of 2 sides
        my_logger(logging): the my_logger
       """
       super().__init__(shape_id, shape_type, my_logger) 
       self.my_logger.info(f"sent shape_id: {shape_id}, shape_type: {shape_type}, my_logger to super() in base class")


       length, width = args[0], args[1]
       if not isinstance(length, (int, float)):
          self.my_logger.error(f"type of {length} should be int/float and not {type(length)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {length} should be int/float and not {type(length)}")
       self.length = length

       if not isinstance(width, (int, float)):
          self.my_logger.error(f"type of {width} should be int/float and not {type(width)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {width} should be int/float and not {type(width)}")
       self.width = width

       self.my_logger.info(f"finished in init in {self.shape_type}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
 
    def get_area(self):
       """
       calculate area of Rectangle

       Returns:
        int/float: area of the Rectangle
       """
       self.my_logger.info(f"in function get_area to get area of {self.shape_type}. shape_id: {self.shape_id}")
       return self.length * self.width
 
    def get_perimeter(self):
       """
       calculate perimeter of Rectangle

       Returns:
            int/float: the perimeter
       """
       self.my_logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}. shape_id: {self.shape_id}")
       return 2 * self.length + 2 * self.width
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.my_logger.info(f"in function to_dict to get dict of {self.shape_type}. shape_id: {self.shape_id}")
       return {'id':self.shape_id, 'type':self.shape_type, 'length/radius':self.length, 'side_width':self.width}
    

    def print_details(self):
       return f"""ID: {self.shape_id}\n
       Type: {self.shape_type}\n
       Side Length:{self.length}\n
       Side Width:{self.width}\n
       Area: {self.get_area():.2f}\n
       Perimeter: {self.get_perimeter():.2f}\n"""
    

    def update_shape(self, new_size_1, new_size_2):
       if new_size_1 is not None:
            self.length = new_size_1
       if new_size_2 is not None:
            self.width = new_size_2


def main():
    my_logger = logger.get_logger("rectangle_my_logger")
    r = Rectangle(1, "rectangle", 2, 4, my_logger)
    print(r.get_area())
    print(r.get_perimeter())
    print(r.to_dict())


if __name__ == "__main__":
   main()