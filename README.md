# APOD websbot
A simple program that pulls info from NASA's Astronomy Picture Of the Day (APOD) website and displays it locally in a GUI built from tkinter
# How to install
This assumes you have python and pip already installed and set up
## Installing required libraries
Download the files in the repository and place all of them in their own directory. Using the command line, navigate to the
newly created directory and run the following in the command line (if you have python3, then you may have to use pip3 instead of pip):
`$ pip install -r requirements.txt` 
# Running the program
To run the program, simply navigate to the directory where the files from this repository are located, and use python to run
APODwebsbot.py like so (if you have python3, simply change python to python3):
`$ python APODwebsbot.py`
# Notes on current version use
Under the current version the image file that the os module looks for is a jpg extention while the image file downloaded may be of extentions jpg, gif, and png.
This means if the file is a png or gif the file won't be displayed but will be downloaded (assuming it's a gif or png). Additionally it assumes there will only be 1 jpg in
the directory so if there is more than 1 the wrong image might be displayed. The last issue is that when the image is displayed in the GUI it may be shown blown up and as such the entire image isn't shown. Future versions will aim to fix all these problems, but be aware the first two may create issues for displaying the image. 
