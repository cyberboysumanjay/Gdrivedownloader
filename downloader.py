import urllib.request
import os
import sys

def get_filename():
    print("Enter the Direct URL of the file you want to download: ")
    url=input()
    print('Beginning file download...')
    print('This may take time depending upon the file size.\nPlease be patient')
    filename = url.split("/")[-1]
    local_download(url,filename)
    return filename

def local_download(url,filename):
    pathname = os.path.dirname(sys.argv[0])
    path=str(os.path.abspath(pathname))+"/"
    try:
        urllib.request.urlretrieve(url, path+str(filename))
    except Exception as e:
        print("Error! Can't proceed further.")
        print("Sorry!")
        print(e)
    else:
        print(filename+ ' is successfully downloaded locally ')
        print('Starting Google Drive upload.....')


def local_delete(filename):
    print('Performing local cleanup.........')
    os.remove(filename)
    print('Everything done... Exiting!')
