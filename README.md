# Thinkific Downloader
Downloads files from Thinkific using the html embed code received from right-clicking on a video and clicking "Copy link and thumbnail"

Use dlguide_parser.py to download multiple videos and organize them into subdirectories
The root directory is the location of the script

In a guide file, use #Folder to create a new folder with name 'Folder'
Use ;Subfolder to create a folder inside 'Folder' with name 'Subfolder'
Then copy the html embed code for each video in the subfolder

See 'example_guide.txt' for an example

To run the example, type: python dlguide_parser.py example_guide.txt
