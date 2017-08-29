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

# MailSend
This script sends notification to a zoho email account when a process in the pre-processing part is finished.
It is composed of a two functions send_email and Metadata

### send_email
This function prepares the components of the email and establishes the connection between the zoho server and the script

### Metadata
This function change the metadata of a HTML file that contains the default information of each images

# FalsePositives
This scritp withdraws of the pixels that was misclassified as water in the processed images 
it consists of a class called FalsePositives and one method called overlay.

### overlay
this method withdraws of the pixels that was misclassified as water in the processed images


