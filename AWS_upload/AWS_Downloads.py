import boto3

AWS_REGION = "eu-west-2"

bucket_name = "hands-on-cloud-task1-bucket2"

# Connetint to s3 bucket
resource = boto3.resource("s3", region_name=AWS_REGION)

object = resource.Object(bucket_name, "/home/zeinab/mockdata.csv")

# Downloading to /tmp directory
object.download_file("/home/zeinab/mockdata.csv")
