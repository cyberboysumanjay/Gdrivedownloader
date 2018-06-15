Google Drive Uploader
=====================

Simple script to upload files on Google Drive through Direct URL and gives the direct drive download link.

# Description
Script uses predefined Drive APIs Client ID and Client Secret

It takes upload file as command line argument, uploads it and sets permissions that anyone who has download link can download the file.  
After file has been uploaded the script prints direct download url.

# Requirements
  * Python >= 2.6 [Tested on Python 3.5]
  * [google-api-python-client](http://code.google.com/p/google-api-python-client/)
  * python-httplib2
  * urllib
  * sys
  * logging
  * mimetypes
  * apiclient
  * oauth2client


# Example Usage:
####  Note: Make sure you've given the bash file permission to execute
> sudo chmod +x start.sh

#### You can also start the file without using bash using the command

>> python3 gdrive_upload.py


  > cyberboy@MonsterMachine:~/python/gdrive/Gdrivedownloader$ ./start.sh
  Enter the Direct URL of the file you want to download:
  https://cyberboysumanjay.github.io/img/jetpacktocat.jpg
  Beginning file download...
  This may take time depending upon the file size.
  Please be patient
  jetpacktocat.jpg is successfully downloaded locally
  Starting Google Drive upload.....
  https://drive.google.com/a/nitdelhi.ac.in/uc?id=1y64hPnzIt_9eYpID5hYL8yg9MPUQKYfc&export=download
  Performing local cleanup.........
  Everything done... Exiting!

# Credits
### kshcherban for his lovely work [here](https://github.com/kshcherban/gdrive_uploader)
