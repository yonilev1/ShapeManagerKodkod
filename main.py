from shape_manager import ShapeManager

def show_welcome():
   """
   show welcome message
   """
   prompt = """
    --------------------------------
    Welcome to Shape Manager System!
    --------------------------------
    """
   print(prompt)


def show_options():
    """
    show option bar
    """
    prompt = """
    option:
    To add a shape - choose 1,
    To edit a shape - choose 2,
    To delete a shape - choose 3,
    To show all shapes - choose 4
    To exit - choose 0
    """
    print(prompt)
 

def main():
 shape_manager = ShapeManager()
 user_loged_in = True
 show_welcome()

 while user_loged_in:
    show_options()
    choice = int(input("Enter your chioce: "))

    match choice:
       case 1:
          shape = input("Enter yout shape [circle, square or rectangle]: ")
          if shape not in ['circle', 'square', 'rectangle']:
             raise ValueError(f"shape has to be one of - [circle, square or rectangle]. you entered: {shape}")
          
          if shape == 'circle':
             radius = int(input("Enter circles radius: "))
             id = shape_manager.create_shape(shape,radius=radius)
             print(f"shape {shape} was created successfully with id: {id}!")

          elif shape == 'square':
             side_length = int(input("Enter squares side length: "))
             shape_manager.create_shape(shape,length=side_length)
             print(f"shape {shape} was created successfully with id: {id}!")

          elif shape == 'rectangle':
             side_length = int(input("Enter rectangles side length: "))
             side_lwidth = int(input("Enter rectangles side width: "))
             shape_manager.create_shape(shape,length=side_length, width=side_lwidth)
             print(f"shape {shape} was created successfully with id: {id}!")
        
       case 2:
          
          
          


