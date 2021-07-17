# EPaiSequence
Sequence Types
# Sequence Types

## Assignment

1. A regular strictly convex polygon is a polygon that has the following characteristics:
    * All interior angles are less than 180
    * All sides have equal length

2. For a regular strictly convex polygon with vertices n and circumradius r:
    * interiorAngle = (n−2) * (180/n)
    * edgeLength, s = 2 * R * sin(π/n) 
    * apothem, a = R * cos(π/n)
    * area = (1/2) * n * a
    * perimeter = n * s
3. **Objective 1**:

     Create a Polygon Class:
     
     1. Where initializer takes in:
        * number of edges/vertices
        * circumradius
      2. That can provide these properties:
          * edges
          * vertices
          * interior angle
          * edge length
          * apothem
          * area
          * perimeter
      3. That has these functionalities:
          * a proper __repr__ function
          * implements equality (==) based on # vertices and circumradius (__eq__)
          * implements > based on number of vertices only (__gt__)
```
class Polygon(builtins.object)
 |  Polygon(n_edges: int, circumradius: float)
 |  
 |     Polygon class to create polygons which are regular strictly convex.
 |     Regular strict polygons have two properties: 
 |  1- All interior angles are less than 180.     
 |  2- All sides have equal length
 |  
 |  Methods defined here:
 |  
 |  __eq__(self, poly)
 |      Provides ability to compare two objects for euality (==).
 |  
 |  __gt__(self, poly)
 |      Provide ability to compare two objects for greater than '>' test.
 |  
 |  __init__(self, n_edges: int, circumradius: float)
 |      Initialize the edges, circumradius, interiorAngle, edgeLength , apothem, area, perimeter.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  apothem
 |      Apothem length for the polygon
 |  
 |  area
 |      Area of the polygon
 |  
 |  circumradius
 |      Circumradius of the polygon
 |  
 |  edge_length
 |      Edge length of individual edge in the polygon
 |  
 |  interior_angle
 |      Interior angle value of each angle in the polygon
 |  
 |  n_edges
 |      Number of edges in the polygon
 |  
 |  perimeter
 |      Perimeter of the polygon
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
```

4. **Objective 2**:
    Implement a Custom Polygon sequence type:
    
    1. Where initializer takes in:
        * number of vertices for largest polygon in the sequence
        * common circumradius for all polygons
        * that can provide these properties:
        * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
     2. that has these functionalities:
        * functions as a sequence type (__getitem__)
        * supports the len() function (__len__)
        * has a proper representation (__repr__)
 ```class Poly_sequence(builtins.object)
 |  Poly_sequence(n_edges: int, circumradius: float)
 |  
 |  Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
 |  by n_edges_max  and circumradius for all polygons is is given by circumradius and is same for all polygons"
 |  
 |  Methods defined here:
 |  
 |  __getitem__(self, edges)
 |      This function returns the properties of the polygon whose vertices, circumradius are as passed in the
 |      arguments. It returns 'Not a polygon' message if the number of vertices is less than 3.
 |  
 |  __init__(self, n_edges: int, circumradius: float)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __len__(self)
 |      This function gives the length of the Polygon Sequence object
 |  
 |  __repr__(self)
 |      This function gives the details of the Polygon Sequence object
 |  
 |  get_polygon(self, n_edges, circumradius)
 |      This function returns the properties of the polygon such as vertex , circumradius, interior angle, edge
 |      length , apothem, area, perimeter as a named tuple.
 |  
 |  max_efficiency(self)
 |      This function returns the maximum efficiency polygon.
 |      Here, a maximum efficiency polygon is one that has the highest area to perimeter ratio.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 
```
p = Poly_sequence(25,5)
p.max_efficiency()
```
**Polygon with 25 vertices has the Max Efficiency of 2.4802867532861947**
