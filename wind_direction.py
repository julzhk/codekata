"""
implement a function to help an aircraft calculate its heading, given a target and wind direction & speed data
"""

import math
import re

def integerize(func):
    def integerize(*args, **kwargs):
        return int(round(func(*args, **kwargs),0))
    return integerize

@integerize
def cross_wind(angle, windspeed):
    return math.sin(angle) * windspeed

@integerize
def head_wind(angle, windspeed):
    return math.cos(angle) * windspeed

def angles_to_radians(degrees):
    return float(degrees * math.pi) / 180

def get_runway_heading_in_degrees(runway_code):
    return 10 * int(re.search(r'\d+', runway_code).group())

def wind_info(runway, wind_direction, wind_speed):
    """
    A = Angle of the wind from the direction of travel (radians)
    WS = Wind speed
    CW = sin(A) * WS : Crosswind
    HW = cos(A) * WS : Headwind

    :param runway: (string): "NN[L/C/R]"). NN is the runway's heading in tens of degrees.
                    A suffix of L, C or R may be present and should be ignored.
                    NN is between 01 and 36.
    :param wind_direction:  (int). Direction wind is blowing from in degrees. Between 0 and 359.
    :param wind_speed:  (int). Wind speed in knots
    :return: "(Head|Tail)wind N knots. Crosswind N knots from your (left|right)."
    """
    runway_angle = get_runway_heading_in_degrees(runway_code=runway)
    wind_direction = wind_direction - runway_angle

    headwind = head_wind(angle=angles_to_radians(wind_direction), windspeed=wind_speed)
    crosswind = cross_wind(angle=angles_to_radians(wind_direction), windspeed=wind_speed)
    return "%(head)swind %(headwind)d knots. Crosswind %(crosswind)s knots from your %(side)s." % {
        'head': 'Head' if headwind >0 else 'Tail',
        'headwind': abs(headwind),
        'crosswind': abs(crosswind),
        'side': 'left' if crosswind < 0 else 'right'
    }

print cross_wind(1.04719755, 15)
print head_wind(1.04719755, 15)

test_data = [
(("18", 170, 15),"Headwind 15 knots. Crosswind 3 knots from your left."),
(("18", 210, 14),"Headwind 12 knots. Crosswind 7 knots from your right."),
(("22L", 160, 14),"Headwind 7 knots. Crosswind 12 knots from your left."),
(("18", 70, 15),"Tailwind 5 knots. Crosswind 14 knots from your left." )
]
for t in test_data:
    print wind_info(*t[0])