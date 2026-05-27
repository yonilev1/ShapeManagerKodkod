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
    try:
        show_options()
        choice = input("Enter your chioce: ")

        match choice:
            case '1':
                shape = int(input("""
            Enter yout shape:
            1- circle,
            2 - square,
            3- rectangle: """))
                if shape not in [1,2,3]:
                    raise ValueError(f"shape has to be one of: 1 (- circle), 2 (- square), 3 (- rectangle). you entered: {shape}")
                
                if shape == 1:
                    radius = int(input("Enter circles radius: "))
                    if radius <= 0:
                        raise ValueError("value cant be <= 0")
                    id = shape_manager.create_shape('circle',radius=radius)
                    print(f"shape {shape} was created successfully with id: {id}!")

                elif shape == 2:
                    side_length = int(input("Enter squares side length: "))
                    if side_length <= 0:
                        raise ValueError("value cant be <= 0")
                    id = shape_manager.create_shape('square',length=side_length)
                    print(f"shape {shape} was created successfully with id: {id}!")

                elif shape == 3:
                    side_length = int(input("Enter rectangles side length: "))
                    if side_length <= 0:
                        raise ValueError("value cant be <= 0")
                    
                    side_lwidth = int(input("Enter rectangles side width: "))
                    if side_lwidth <= 0:
                        raise ValueError("value cant be <= 0")
                    
                    id = shape_manager.create_shape('rectangle',length=side_length, width=side_lwidth)
                    print(f"shape {shape} was created successfully with id: {id}!")

            case '2':
                shape_manager.get_all_shapes()

            case '3':
                id = int(input("Enter shapes id to update: "))
                side_1 = int(input("Enter the length/radius to update: "))
                if side_1 <= 0:
                        raise ValueError("value cant be <= 0")
                
                side_2 = int(input("Enter the width to update (if square or circle, put -1): "))
                if side_2 == 0 or side_2 < -1:
                        raise ValueError("value cant be 0 or less then -1")
                
                if side_2 == -1:
                    side_2 = None

                did_update = shape_manager.update_shape(id, side_1, side_2)
                if did_update:
                    print(f"shape {id} was edited successfully!")

            case '4':
                id = int(input("Enter shapes id to delete: "))
                did_delete = shape_manager.delete_shape(id)
                if did_delete:
                    print(f"shape {id} was deleted successfully!")

            case '0':
                user_loged_in = False

            case _:
                print("choice not valid. choose again.")
    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)          

if __name__ == "__main__":
   main()
          
          


