import math


def len_of_side(length, no_of_sides):
    a = ((length*length)*no_of_sides)/(4*math.tan(180/no_of_sides))
    return a


def radius(radius_length, no_of_sides):
    a = (radius_length*radius_length)*no_of_sides*(math.sin(360/no_of_sides))
    return a


def apothem(len_of_apothem, no_of_sides):
    a = (len_of_apothem*len_of_apothem)*no_of_sides*(math.tan(180/no_of_sides))
    return a
