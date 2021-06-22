# APOD websbot
A simple program that pulls info from NASA's Astronomy Picture Of the Day (APOD) website and displays it locally in a GUI built from tkinter
# How to install
This assumes you have python and pip already installed and set up
## Installing required libraries
Download the files in the repository and place all of them in their own directory. Nativate to the newly created directory using a command line and use pip to install all 
the important modules which are specified in `requirements.txt`
# Running the program
To run the program, simply navigate to the directory where the files from this repository are located, and use python to run
APODwebsbot.py. It takes a few seconds then the GUI will appear with the information and a button to click to display the picture of the day
# Notes on current version use
Under the current version the image file downloaded can be of file extentions jpg, gif, and png but the os module of the program only looks for 1 jpg to display.
This means an image file can be downloaded but won't be displayed when the button to do so is pressed. If there is more than 1 jpg files the wrong picture might get displayed.
Additionally there is an issue with the 6/21/2021 APOD image being blown way up causing only a portion of the image to be displayed on the whole screen. This issue may persist 
for other images but this is yet untested. A future update is planned to fix these known issues. 
