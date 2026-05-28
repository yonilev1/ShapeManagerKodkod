import shape
import logger

class Square(shape.Shape):
    """
    class square, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, length, my_logger): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        length(int/float): the length of every Side
        my_logger(logging): the my_logger
       """
       super().__init__(shape_id, shape_type, my_logger)
       self.my_logger.info(f"sent shape_id: {shape_id}, shape_type: {shape_type}, my_logger to super() in base class")

       if not isinstance(length, (int, float)):
          self.my_logger.error(f"type of {length} should be int/float and not {type(length)}. shape_id: {self.shape_id}, shape_type: {self.shape_type}")
          raise ValueError(f"type of {length} should be int and not {type(length)}")
         
       self.length = length
       self.my_logger.info(f"finished in init in {self.shape_type}. shape_id: {self.shape_id}")
 
    def get_area(self):
       """
       calculate area of square

       Returns:
        int/float: area of the square
       """
       self.my_logger.info(f"in function get_area to get area of {self.shape_type}. shape_id: {self.shape_id}")
       return self.length * self.length
 
    def get_perimeter(self):
       """
       calculate perimeter of square

       Returns:
            int/float: the perimeter
       """
       self.my_logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}. shape_id: {self.shape_id}")
       return 4 * self.length 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.my_logger.info(f"in function to_dict to get dict of {self.shape_type}. shape_id: {self.shape_id}")
       return {'id':self.shape_id, 'type':self.shape_type, 'side':self.length}
    

   
def main():
    my_logger = logger.get_logger("square_my_logger")
    s = Square(1, "square", 2, my_logger)
    print(s.get_area())
    print(s.get_perimeter())
    print(s.to_dict())


if __name__ == "__main__":
   main()