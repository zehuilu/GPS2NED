# -*- coding: UTF-8 -*-

"""

Author: ZEHUI LU

An example about how to use the module 'transformation_GPS' to transform 
the GPS coordinates to the local North-East-Down (NED) coordinates.

"""

import numpy as np
import transformation_GPS as tran_GPS


if __name__ == '__main__':

    # define your own GPS coordinates, at least 2 points
    # one is the home/origin, another is the one you are interested in 
    # you need to define home_latitude [decimal degree], home_longitude [decimal degree], and home_altitude [meter]

    # set the origin for NED, the ECEF (Earth-Centered, Earth-Fixed) coordinates are the intermediate ones
    # R_ECEF2NED will be used whenever you want to fransfrom the GPS coordinates
    origin_ECEF, R_ECEF2NED = tran_GPS.GPS2ECEF(home_latitude, home_longitude, home_altitude, 1)

    # you need to define another interested point with GPS coordinates, la_1, lo_1, al_1
    point_NED_1 = tran_GPS.GPS2NED(la_1, lo_1, al_1, origin_ECEF, R_ECEF2NED)

    point_NED_2 = tran_GPS.GPS2NED(la_2, lo_2, al_2, origin_ECEF, R_ECEF2NED)