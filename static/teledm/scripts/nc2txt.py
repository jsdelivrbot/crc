#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import os

from netCDF4 import Dataset, num2date
import pandas as pd
import numpy as np



try:
    fichier = sys.argv[1]
except IndexError:
    sys.exit('Fichier impossible a ouvrir')

path = os.path.dirname(os.path.abspath(fichier))

nc = Dataset(fichier, 'r')
var = list(set(nc.variables.keys()) - set(['time', 'latitude', 'longitude']))[0]
dt = nc.variables['time']
dates = num2date(dt[:], dt.units)
arr = nc.variables[var][:].filled(np.nan)
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
x,y = np.meshgrid(lon,lat)
pxIndex = [str(ll) for ll in zip(x.flatten(),y.flatten())]
df = pd.DataFrame(arr.reshape(dates.size,-1), index=dates, columns=pxIndex)
df.to_csv('test.csv', header=True, index=True, index_label='date')
nc.close()
