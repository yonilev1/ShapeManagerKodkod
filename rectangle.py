import shape

class Rectangle(shape.Shape):
    """
    class rectangle, inharits from class Shape
    """
    def __init__(self, shape_id, shape_type, length, witdth): 
       """
       init function 

       Args:
        shape_id(int): id of shape
        shape_type(str): type of the shape
        length(int/float): the length of 2 Sides
        width(int/float): the width of 2 sides
       """
       self.shape_id = shape_id 
       self.shape_type = shape_type 
       self.length = length
       self.width = witdth
 
    def get_area(self):
       """
       calculate area of Rectangle

       Returns:
        int/float: area of the Rectangle
       """
       return self.length * self.width / 2 
 
    def get_perimeter(self):
       """
       calculate perimeter of Rectangle

       Returns:
            int/float: the perimeter
       """
       return 4 * self.length 
 
    def to_dict(self): 
       """
       Returns:
        a dict with the data of the shape to store in the DB
       """
       return {'id':self.shape_id, 'type':self.shape_type, 'side_length':self.length, 'side_width':self.width} 

 