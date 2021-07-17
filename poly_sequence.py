from polygon import *
from functools import lru_cache
from collections import namedtuple


@validate_params
class Poly_sequence:
    """
    Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
    by n_edges_max  and circumradius for all polygons is is given by circumradius and is same for all polygons"
    """
    def __init__(self, n_edges: int, circumradius: float):
        self._n_edges = n_edges
        self._circumradius = circumradius

    @lru_cache(maxsize=2**10)
    def get_polygon(self, n_edges, circumradius):
        """ This function returns the properties of the polygon such as vertex , circumradius, interior angle, edge
        length , apothem, area, perimeter as a named tuple.
        """
        polygon = Polygon(n_edges, circumradius)
        interiorangle = polygon.interior_angle
        edgelength = polygon.edge_length
        apothem = polygon.apothem
        area = polygon.area
        perimeter = polygon.perimeter

        prop_names = ('vertex', 'circumradius', 'interiorAngle', 'edgeLength', 'apothem', 'area', 'perimeter')
        properties = namedtuple('Polygon', prop_names)

        # print(f'Calculating for Polygon with Vertex:{n_edges} , CircumRadius: {circumradius}')
        return properties(n_edges, circumradius, interiorangle, edgelength, apothem, area, perimeter)

    def max_efficiency(self):
        """ This function returns the maximum efficiency polygon.
        Here, a maximum efficiency polygon is one that has the highest area to perimeter ratio.
        """

        ratios = []

        for i in range(3, self._n_edges+1):
            """ This function """
            p = self.get_polygon(i, self._circumradius)
            ratios.append(p.area/p.perimeter)
            # print(ratios)
        max_index = max(range(len(ratios)), key=ratios.__getitem__)
        # print(ratios)
        print(f'Polygon with {max_index+3} vertices has the Max Efficiency of {ratios[max_index]}')

    def __getitem__(self, edges):
        """ This function returns the properties of the polygon whose vertices, circumradius are as passed in the
        arguments. It returns 'Not a polygon' message if the number of vertices is less than 3.
        """

        if not isinstance(edges, int):
            return 'Error: Incorrect type for parameter '
        elif edges < 3:
            return 'Error: This is not a polygon'
        else:
            return self.get_polygon(edges, self._circumradius)

    def __repr__(self):
        """ This function gives the details of the Polygon Sequence object"""

        return f""" Contains {self._n_edges} polygons with a circumradius of {self._circumradius} \
         and vertices ranging from 3 to {self._n_edges}"""

    def __len__(self):
        """ This function gives the length of the Polygon Sequence object """

        return self._n_edges
