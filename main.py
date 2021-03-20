from flight_plan_generator import get_best_route

if __name__ == "__main__":
    test_polygon = list(eval(str(input("Input polygon's coordinates in the format [(x,y),(x',y')...] : "))))
    vision_radius = float(input("Input the vision radius (min: 0.5, other values need to be multiples of 0.5): "))
    get_best_route(vertices=test_polygon,
                   vision_radious=vision_radius,
                   debug=True)
