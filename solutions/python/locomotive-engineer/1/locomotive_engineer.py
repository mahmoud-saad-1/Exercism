"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*ids):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *wagons, = ids
    return wagons

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_to_end, second_to_end, first, *rest = each_wagons_id
    *new_order, = first, *missing_wagons, *rest, first_to_end, second_to_end
    return new_order


def add_missing_stops(routing, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    routing["stops"] = list(stops.values())
    return routing


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route = {**route, **more_route_information}
    return extended_route

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    updated_wagons = []
    for row in zip(*wagons_rows):
        updated_wagons.append(list(row))
    return updated_wagons
