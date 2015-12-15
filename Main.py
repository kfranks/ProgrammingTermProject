#!/usr/bin/env python
# Katy Franks, Alex Holland, Parker Pennington 
import arcpy
import functions
from arcpy import env
env.workspace=r'E:\SP_Landsat'
filelist=['las_vegas.tif','Lincoln.tif','SLC.tif','Tucsaloosa.tif']
for x in filelist:
  functions.unsup(x)
for x in filelist:
  gsg=x.split('.')[0]+'.gsg'
  functions.maxlik(x,gsg)
