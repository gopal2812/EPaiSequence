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
