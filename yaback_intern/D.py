import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point[x={}, y={}]".format(self.x, self.y)


class Segment:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return "Segment[start = {}, end = {}".format(self.start_point, self.end_point)


class Vector:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.x_component = end_point.x-start_point.x
        self.y_component = end_point.y - start_point.y

    def __str__(self):
        return "Vector [start = {}, end = {}]".format(self.start_point, self.end_point)


def vector_cross_product(vector_1, vector_2):
    return vector_1.x_component * vector_2.y_component - vector_2.x_component * vector_1.y_component


def range_intersection(range_1_s, range_1_e, range_2_s, range_2_e):
    if range_1_s > range_1_e:
        range_1_s, range_1_e = range_1_e, range_1_s
    if range_2_s > range_2_e:
        range_2_s, range_2_e = range_2_e, range_2_s
    return max(range_1_s, range_2_s) <= min(range_1_e, range_2_e)


def bounding_box(segment_1, segment_2):
    x1 = segment_1.start_point.x
    x2 = segment_1.end_point.x
    x3 = segment_2.start_point.x
    x4 = segment_2.end_point.x
    y1 = segment_1.start_point.y
    y2 = segment_1.end_point.y
    y3 = segment_2.start_point.y
    y4 = segment_2.end_point.y
    return range_intersection(x1, x2, x3, x4) and range_intersection(y1, y2, y3, y4)


def check_segment_intersection(segment_1, segment_2):
    if not bounding_box(segment_1, segment_2):
        return False
    vector_ab = Vector(segment_1.start_point, segment_1.end_point)
    vector_ac = Vector(segment_1.start_point, segment_2.start_point)
    vector_ad = Vector(segment_1.start_point, segment_2.end_point)

    vector_cd = Vector(segment_2.start_point, segment_2.end_point)
    vector_ca = Vector(segment_2.start_point, segment_1.start_point)
    vector_cb = Vector(segment_2.start_point, segment_1 .end_point)

    d1 = vector_cross_product(vector_ab, vector_ac)
    d2 = vector_cross_product(vector_ab, vector_ad)
    d3 = vector_cross_product(vector_cd, vector_ca)
    d4 = vector_cross_product(vector_cd, vector_cb)

    if ((d1 <= 0 and d2 >= 0) or (d1 >= 0 and d2 <= 0)) and ((d3 <= 0 and d4 >= 0) or (d3 >= 0 and d4 <= 0)):
        return True
    return False


point_a = Point(1, 2)
point_b = Point(3, 3)
point_c = Point(1, 1)
point_d = Point(4, 3)

segment_1 = Segment(point_a, point_b)
segment_2 = Segment(point_c, point_d)

print(check_segment_intersection(segment_1, segment_2))
