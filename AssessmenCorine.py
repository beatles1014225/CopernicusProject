import arcpy
from arcpy.sa import *
from os import listdir
import glob
class ConfusionMatrix(object):
    def __init__(self, fileName):
        self.name = fileName
        self.path = "D:\\Diego\\MASTER\\COPERNICUS\\Classification Assessment\\ResultsAssesment\\Results2\\"
        self.WaterBodiesDetected = "D:\\Diego\\MASTER\\COPERNICUS\\Classification Assessment\\Downloads\\FinalTest\\" + self.name


    ##To clip the general raster truth image    
    def clipTrue(self):
        
        self.clipRaster = arcpy.Clip_management("D:\Diego\MASTER\COPERNICUS\Classification Assessment\Corine\g100_clc12_V18_5a\g100_clc12_V18_5.tif", '#',
                                                "#",
                                                self.WaterBodiesDetected,"ClippingGeometry")
        attExtract = ExtractByAttributes(self.clipRaster, "VALUE = 40 Or VALUE = 41 Or VALUE = 44") 

        
        outraster = Con(IsNull(attExtract), 0, 100)
        self.nameTV = self.name.rsplit(".")[0] + "TV" + ".tif"
        outraster.save(self.path + self.nameTV)
        

    ##To create assessment point with truth values
    def AssessmentPoints(self):
       arcpy.gp.CreateAccuracyAssessmentPoints(Raster(self.path + self.nameTV), self.path + self.name.rsplit(".")[0] + "point" , "GROUND_TRUTH", "6000", "STRATIFIED_RANDOM")
        
    ##To update assessment point with classified values
    def UpdateAssessmentPoints(self):
       arcpy.gp.UpdateAccuracyAssessmentPoints(self.WaterBodiesDetected, self.path + self.name.rsplit(".")[0] + "point.shp",
                                        self.path + self.name.rsplit(".")[0] + "point2", "CLASSIFIED")
    ##To calculate confusion matrix

    def ConfusionMatrix(self):
        arcpy.gp.ComputeConfusionMatrix(self.path + self.name.rsplit(".")[0] + "point2.shp", self.path + self.name.rsplit(".")[0] + "confMatrix.dbf")



files = glob.glob("D:\\Diego\\MASTER\\COPERNICUS\\Classification Assessment\\Downloads\\FinalTest\\*.tif")
for fls in files:
    fileName = fls.rsplit("FinalTest\\")[1]
    test = ConfusionMatrix(fileName)
    test.clipTrue()
    test.AssessmentPoints()
    test.UpdateAssessmentPoints()
    test.ConfusionMatrix()
    print(fileName)
