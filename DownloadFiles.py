import boto3
from MailSend import*
configuration = getDefaultConfigurationFile()
processXMLPath = configuration["processXMLPath"]
inputPath = configuration["inputPath"]
outputPath = configuration["outputPath"]
processStatusPath = configuration["processStatusPath"]
safeFileExtension = configuration["safeFileExtension"]
zipFileExtension = configuration["zipFileExtension"]
outputFileExtension = configuration["outputFileExtension"]
exportFileExtension = configuration["exportFileExtension"]
BUCKET_NAME_RAW_IMAGES = configuration["BUCKET_NAME_RAW_IMAGES"]
BUCKET_NAME_PROCESSED_IMAGES = configuration["BUCKET_NAME_PROCESSED_IMAGES"]
BUCKET_FOLDER_NAME_PREPROCESSED_IMAGES = configuration["BUCKET_FOLDER_NAME_PREPROCESSED_IMAGES"]
MAX_PREPROCESSING_ATTEMPTS = int(configuration["MAX_PREPROCESSING_ATTEMPTS"])
META_DATA_STATUS_KEY = configuration["META_DATA_STATUS_KEY"]
META_DATA_ATTEMPTS_KEY = configuration["META_DATA_ATTEMPTS_KEY"]
MAIL_ACCOUNT_SENDER = configuration["MAIL_ACCOUNT_SENDER"]
MAIL_ACCOUNT_PASSWORD = configuration["MAIL_ACCOUNT_PASSWORD"]
MAIL_ACCOUNT_RECIVER = configuration["MAIL_ACCOUNT_RECIVER"]

session = boto3.Session(aws_access_key_id="MYACCESSKEY", aws_secret_access_key="MYSECRETACCESSKEY")
s3 = session.resource('s3')
buck = s3.Bucket("teambtestbucket")
for object in buck.objects.all():
    filename = object.key
    if("preprocessed-images" in filename):
        pass
    else:
        print(object.key.rsplit('/')[-1])
        buck.download_file(filename, "D:\\Diego\\MASTER\\COPERNICUS\\Classification Assessment\\DownloadWOWB\\" + object.key.rsplit('/')[-1])



