import urllib.request
import os
import sys
import subprocess
import wget

def start():
    url=input("Enter the Direct URL of the file you want to download: ")
    print('Beginning file download...')
    print('This may take time depending upon the file size.\nPlease be patient')
    filename=local_download(url)
    return filename

def local_download(url):
    filename='none'
    try:
        filename=wget.download(url)
    except Exception as e:
        print("Error! Unable to download file.")
        print(e)
    else:
        print(filename+ ' is successfully downloaded locally ')
        print('Starting Google Drive upload.....')
    return filename


def local_delete(filename):
    print('Performing local cleanup.........')
    os.remove(filename)
    print('Everything done... \nExiting!')
