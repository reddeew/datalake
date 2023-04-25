# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def download_file(dir,path):
  try:
    #file_name = 'song-dat/A/B/N/TRABNLE128EF34B85D.json'
    #path = 'C://Users//91810//Desktop//udacity//file.txt'
    s3.meta.client.download_file(bucket_name,file_name,path)
  except:
   print("An Exception occured")

def list_file(bucket_name,dir_name):
  try:
      s3 = boto3.resource('s3')
      my_bucket = s3.Bucket('bucket_namee')
      for object_summary in my_bucket.objects.filter(Prefix="dir_name/"):
          print(object_summary.key)
  except:
   print("An Exception occured")
# Press the green button in the gutter to run the script.
#download_file(dir,path)
list_file('udacity-dend','song-data')


# Create an S3 resource
s3 = boto3.resource('s3')

# Set the name of the bucket and directory you want to list the contents of
bucket_name = 'udacity-dend'
directory_name = 'song_data'
log_data=log_data/2018/11/2018-11-12-events.json
if __name__ == '__main__':
    print('Welcome to udacity Datalake')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
