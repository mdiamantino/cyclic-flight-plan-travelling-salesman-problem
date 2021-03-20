from __future__ import print_function
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import matplotlib.pyplot as plt
import sympy
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import LineString


def create_data_model(coordinates):
    """
    Stores the data for the problem.
    :param coordinates: List of int 2-tuples (x,y) of coordinates
    :return: Model data dictionary
    """
    data = dict()
    data['locations'] = coordinates
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def is_path_in_polygon(polyg, p1, p2):
    seg = LineString([p1, p2])
    return seg.within(polyg)


def compute_euclidean_distance_matrix(p, locations, isconvex):
    """
    Creates callback to return distance between points.
    :param locations:
    :return: Dictionary of dictionaries {node_index:{dest_node_index:distance, ..} ……}
    """
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:  # If same, dist = 0
                distances[from_counter][to_counter] = 0
            else:  # Otherwise, compute euclidean distance (distance is multiplied by 100, because only works with INT)
                if not isconvex and not (is_path_in_polygon(p, from_node, to_node)):
                    distances[from_counter][to_counter] = 9999999
                else:
                    distances[from_counter][to_counter] = int(100 * (
                        math.hypot((from_node[0] - to_node[0]), (from_node[1] - to_node[1]))))
    return distances


def list_all_points_inside_polyg(polyg_choords, vision_radius=0.5):
    polygon = Polygon(polyg_choords)
    inside_points = []
    xmin, ymin, xmax, ymax = polygon.bounds
    try:
        for i in range(int(ymin), int(ymax) + 1, int(vision_radius * 2)):
            for j in range(int(xmin), int(xmax) + 1, int(vision_radius * 2)):
                if polygon.contains(Point((j, i))):
                    inside_points.append((j, i))
    except ValueError:
        print("Please, choose a 'vision_radius' multiple of 0.5 (where 0.5 is the minimum value)")
    return inside_points


def compute_route(points, manager, routing, assignment):
    index = routing.Start(0)
    # route_distance = 0
    ordered_points = []
    while not routing.IsEnd(index):
        ordered_points.append(points[manager.IndexToNode(index)])
        index = assignment.Value(routing.NextVar(index))
    ordered_points.append(points[manager.IndexToNode(index)])
    return ordered_points


def print_solution(ordered_points, poly):
    pretty_print = ' -> '.join([str(point) for point in ordered_points])
    for i in range(len(ordered_points) - 1):
        point = ordered_points[i]
        next_point = ordered_points[i + 1]
        if not (is_path_in_polygon(poly, point, next_point)):
            print(point, next_point)
        plt.plot((point[0], next_point[0]), (point[1], next_point[1]), 'ro-')
    print(pretty_print + '\n')
    plt.show()


def plot(vertices):
    for i in range(len(vertices) - 1):
        point = vertices[i]
        next_point = vertices[i + 1]
        plt.plot((point[0], next_point[0]), (point[1], next_point[1]), 'ro-')
    plt.plot((next_point[0], vertices[0][0]), (next_point[1], vertices[0][1]), 'ro-')


def get_best_route(vertices, vision_radious=0.5, debug=False):
    plot(vertices)
    points = list_all_points_inside_polyg(vertices, vision_radious)

    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(points)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(Polygon(vertices), data['locations'],
                                                        sympy.Polygon(*vertices).is_convex())

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.

        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    ordered_points = compute_route(points, manager, routing, assignment)

    if assignment and debug:
        print_solution(ordered_points, Polygon(vertices))
    return ordered_points
