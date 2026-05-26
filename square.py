import shape

class Square(shape.Shape):
    """
    class square, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, length, logger): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        length(int/float): the length of every Side
        logger(logging): the logger
       """
       super().__init__(shape_id, shape_type, logger)  
       self.length = length
 
    def get_area(self):
       """
       calculate area of square

       Returns:
        int/float: area of the square
       """
       return self.length * self.length / 2 
 
    def get_perimeter(self):
       """
       calculate perimeter of square

       Returns:
            int/float: the perimeter
       """
       return 4 * self.length 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       return {'id':self.shape_id, 'type':self.shape_type, 'side':self.length} 

 