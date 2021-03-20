from flight_plan_generator import get_best_route

if __name__ == "__main__":
    test_polygon = [(0, 0), (6, 10), (6, 20), (10, 10), (10, 20), (14, 10), (14, 20), (20, 10), (14, 0), (14, 6)]
    get_best_route(vertices=test_polygon,
                   vision_radious=0.5,
                   debug=True)
