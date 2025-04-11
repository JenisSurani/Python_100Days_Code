# this is the copy version of the curl command in your cmd
import argparse
import requests
import sys

parser=argparse.ArgumentParser()

parser.add_argument("url",help="Give url to download your file")
# means output argument is optional
parser.add_argument("output",nargs="?",help="Give file name as you want to save your download file",default=None)

args=parser.parse_args() # object of namespace class
print(args)

# this function takes url and file_name and download it from web 
def DownloadFile(url,local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1] # take name from the url from last word
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    sys.stdout.write("file downloaded sucessfully")
    return

print(args.output,type(args.output))
DownloadFile(args.url,args.output)


# Author : Jenis Surani
# Topic  : CommandLineUtility
# Date   : 25/02/2025
