# ProgrammingTermProject
#Term project for Spatial Programming 2016.
import os
import arcpy 
from arcpy.sa import *
def unsup(inraster):
  classes=8
  outunsuper=IsoClusterUnsupervisedClassification(inraster,classes,'','','%outsuper.gsg'%(inraster))
  
