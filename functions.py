# ProgrammingTermProject
#Term project for Spatial Programming 2016.
import os
import arcpy 
from arcpy.sa import *

# Perform the unsupervised classification to obtain a .gsg file for the maximum likelihood classification that will be performed next
# Classes for unsupervised classification: water, grasslands, trees, urban, suburban, mountainous terrain, cropland, barren
def unsup(inraster):
  classes = 8
  outunsuper = IsoClusterUnsupervisedClassification(inraster,classes,'','','','%outunsuper.gsg'%(inraster))
  
# Perform the maximum likelihood classification and outputting a confidence raster along with the classification raster. 
def maxlik(inraster,sigfile): 
  
  mlcOut = MLClassify(inraster, sigfile, "", "","", outConfidence,'%outConf.tif'%(outConfidence),'%maxlikeout.tif'%(inraster))
  
  
