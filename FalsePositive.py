import arcpy
from arcpy.sa import *
from arcpy import env

class FalsePositives(object):

    def __init__(self):
        ## Read the image that was already preprocessed
        self.raster = "D:\Diego\MASTER\COPERNICUS\RasterFunctions\outexpanded.tif"
    def overlay(self):
        ## Read the layer with the true values
        inMaskData = "D:\Diego\MASTER\COPERNICUS\RasterFunctions\ShapesNRW\FP_raster\FP_singleValue.tif"
        #outExtractByMask = ExtractByMask(self.raster, inMaskData)
        overlayRaster = FuzzyOverlay([self.raster, inMaskData], 'AND')
        overlayRaster.save("D:\Diego\MASTER\COPERNICUS\Test\OvR.tif")
        ## set the null values
        outraster = SetNull(IsNull(self.raster)| ~IsNull(overlayRaster),self.raster)
        outraster.save("D:\Diego\MASTER\COPERNICUS\Test\OR.tif")

test1 = FalsePositives()
test1.overlay()



