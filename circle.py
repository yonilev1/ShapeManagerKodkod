import shape

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
       self.radius = radius
 
    def get_area(self):
       """
       calculate area of circle

       Returns:
        int/float: area of the circle
       """
       return self.length * self.width / 2 
 
    def get_perimeter(self):
       """
       calculate perimeter of circle

       Returns:
            int/float: the circle
       """
       return 4 * self.length 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       return {'id':self.shape_id, 'type':self.shape_type, 'radius':self.radius}
 