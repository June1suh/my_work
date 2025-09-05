from Shapes import Rectangle, Circle, Triangle
from Utils import larger_shape, convert_unit
def main():
    storage=[]
    print("Welcome to the Shape Tool Kit!")
    which_shape = input("Which shape would you like to create? (rectangle/circle/triangle): ").strip().lower()
    while True:
        if which_shape not in ["rectangle", "circle", "triangle"]:
            print("Invalid shape type. Run the program again.")
        elif which_shape=="rectangle":
            width = int(input("Enter the width of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            shape = Rectangle(width, height)
        elif which_shape=="circle":
            radius = float(input("Enter the radius of the circle: "))
            shape = Circle(radius)
        else:  # triangle
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            shape = Triangle(base, height)

        shape.describe()
        print(f"Area: {shape.area()}")
        storage.append(shape.area())
        if len(storage)==3:
            print("You've reached the maximum number of shapes (3).")
            break
        else:
            another = input("Would you like to create another shape? (yes/no): ").strip().lower()
            if another != "yes":
                break
            elif another == "yes":
                which_shape = input("Which shape would you like to create? (rectangle/circle/triangle): ").strip().lower()
        
    

    # Compare areas
    if len(storage)>1:
        largest = larger_shape(storage[0], storage[1])
        print(f"The largest area among the shapes is: {largest}")
    else: 
        print("Not enough shapes to compare areas.")

    # Convert area of rectangle from cm^2 to m^2
    convert_=input("Would you like to convert the area of the rectangle(if you have one) from square meters to square centimeters? (yes/no): ").strip().lower()
    if convert_=="yes":
        what_=input("Which shape(rectangle)'s area would you like to convert? (Shape1/Shape2/Shape3): ").strip().lower()
        if what_=="shape1":
            rect_area_m2 = convert_unit(storage[0])
        elif what_=="shape2":
            rect_area_m2 = convert_unit(storage[1])
        else:
            rect_area_m2 = convert_unit(storage[2])
    print(f"Rectangle area in square centimeters: {rect_area_m2} cm^2")
main()