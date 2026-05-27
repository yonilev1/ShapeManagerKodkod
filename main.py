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
    To show all shapes - choose 2,
    To update a shape - choose 3,
    To delete a shape - choose 4
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
          shape = int(input("""
    Enter yout shape:
    1- circle,
    2 - square,
    3- rectangle: """))
          if shape not in [1,2,3]:
             raise ValueError(f"shape has to be one of: 1 (- circle), 2 (- square), 3 (- rectangle). you entered: {shape}")
          
          if shape == 1:
             radius = int(input("Enter circles radius: "))
             id = shape_manager.create_shape(shape,radius=radius)
             print(f"shape {shape} was created successfully with id: {id}!")

          elif shape == 2:
             side_length = int(input("Enter squares side length: "))
             shape_manager.create_shape(shape,length=side_length)
             print(f"shape {shape} was created successfully with id: {id}!")

          elif shape == 3:
             side_length = int(input("Enter rectangles side length: "))
             side_lwidth = int(input("Enter rectangles side width: "))
             shape_manager.create_shape(shape,length=side_length, width=side_lwidth)
             print(f"shape {shape} was created successfully with id: {id}!")

        
       case 2:
          shape_manager.get_all_shapes()

       case 3:
          id = int(input("Enter shapes id to update: "))
          side_1 = int(input("Enter the length/radius to update: "))
          side_2 = int(input("Enter the width to update (if square or circle, put -1): "))
          if side_2 == -1: side_2 = None
          shape_manager.update_shape(id, side_1, side_2)
          print(f"shape {shape} was edited successfully!")

       case 4:
          id = int(input("Enter shapes id to delete: "))
          shape_manager.delete_shape(id)
          print(f"shape {shape} was deleted successfully!")

       case 0:
          user_loged_in = False

       case _:
          continue
          

if __name__ == "__main__":
   main()
          
          


