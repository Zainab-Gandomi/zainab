import boto3

AWS_REGION = "eu-west-2"

client = boto3.client("s3", region_name=AWS_REGION)

#creating bucket using Boto3 client

bucket_name = "hands-on-cloud-task1-bucket2"
location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")

# Getting bucket list

response = client.list_buckets()

print("Listing Amazon S3 Buckets:")

for bucket in response['Buckets']:
print(f"-- {bucket['Name']}")


# Printing each bucket
for bucket in response["Buckets"]:
print(f"-- {bucket['Name']}")

# Upload files to bucket
def upload_files(file_name, bucket, object_name=None, args=None):
if object_name is None:
object_name = file_name

client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
print(f"'{file_name}' has been uploaded to '{bucket_name}'")

upload_files(f"/home/zeinab/mockdata.csv", bucket_name)


# Uploading modified file
upload_files('/home/zeinab/mockdata.csv', bucket_name)
