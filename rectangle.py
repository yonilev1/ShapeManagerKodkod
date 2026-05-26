import shape

class Rectangle(shape.Shape):
    """
    class rectangle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, length, witdth, logger): 
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
       self.logger.info("sent shape_id, shape_type, logger to super() in base class")
       self.length = length
       self.width = witdth
       self.logger.info(f"finished in init in {shape_type}")
 
    def get_area(self):
       """
       calculate area of Rectangle

       Returns:
        int/float: area of the Rectangle
       """
       self.logger.info(f"in function get_area to get area of {self.shape_type}")
       return self.length * self.width / 2 
 
    def get_perimeter(self):
       """
       calculate perimeter of Rectangle

       Returns:
            int/float: the perimeter
       """
       self.logger.info(f"in function get_perimeter to get perimeter of {self.shape_type}")
       return 4 * self.length 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       self.logger.info(f"in function to_dict to get dict of {self.shape_type}")
       return {'id':self.shape_id, 'type':self.shape_type, 'side_length':self.length, 'side_width':self.width} 

 