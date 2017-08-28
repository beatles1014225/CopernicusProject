# AssessmentCorine 
This Python script contains the code to carry out all concerning the assessment process.
It is compesed of a class called ConfusionMatrix that contains the methods clipTrue, AssessmentPoints, UpdateAssessmentPoints and ConfusionMatrix
### clipTrue
This method creates a clip of the Corine layer based on the image that was already processed by the water detection procedure.
### AssessmentPoints
This method creates 6000 points to copy the information of the Corine layer.
### UpdateAssessmentPoints
This method uses the 6000 points created previously to copy the information from the image.
### AssessmentCorine 
This method creates the confusion matrix based on the information previously created.

# DownloadFiles
This code creates access to the Amazon bucket to donwload all the images that have been already processed
