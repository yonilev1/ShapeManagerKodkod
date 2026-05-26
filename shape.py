class Shape: 
   def __init__(self, shape_id, shape_type, logger): 
       self.id = shape_id 
       self.shape_type = shape_type 
       self.logger = logger
 
   def get_area(self): 
       pass 
 
   def get_perimeter(self): 
       pass 
 
   def to_dict(self): 
       pass 