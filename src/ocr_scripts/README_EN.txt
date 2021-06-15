Requirements:

- Have python installed (minimum version 3.6.0) 
- Use only jpeg/jpg and png images

-----------------------------------------------------------------------------------
Program structure:

OCR
   |--- ocr.py
   |--- reader.py
   |--- stats.py
   |--- log_handler.py
   |--- installModules.bat
   |--- requirements.txt
   |--- Tesseract-OCR
   |--- README.txt
   |--- log/
   |--- scans/

ocr.py is the file in which all the main operations are handled: it receives the arguments, scans the passed images and puts the resulting text in the output text file. 

log_handler is the file in which the logs for the files (app_debug.log for the debug level; app.log for the info level) and the log on cli for the user are defined and managed.

The files reader.py and stats.py are the modules that contain the methods for image scanning, output management and execution statistics.

The script installModules.bat is used to install with one click the dependencies (contained in the requirements.txt file) that OCR needs to function.

The text file README.txt contains the main information on how to use the programme and the minimum resolution of the images to be scanned.

After the first run, the log and scans folders will be created (scans will not be created if the user specifies a different folder) because these are the default folders for storing log and text files respectively when the output path is not specified.

-----------------------------------------------------------------------------------
How to start the program:

You need to go to the path of the ocr.py and start it with cmd.
If the dependencies are missing, just run "installingModules.bat" which will install them automatically.

-----------------------------------------------------------------------------------
Rules to follow for best results 

- Use images with dark text on a light background
- Tesseract works best on images that have a DPI of at least 300 dpi
- Edges of scanned images may be detected as extra characters
- A font size between 25 and 40 pixels is recommended
- Words with sticky letters are not always recognised
