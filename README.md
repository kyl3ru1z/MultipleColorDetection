# MultipleColorDetection
Uses OpenCV to detect multiple colors in real-time. In this program I am able to put three different colored markers in front of my webcam (orange, green, and purple) and it is able to differentiate between the colors and put the correct text on top of the respected color. 

# How To Use
- I recommend using my HSV Color finder to get the exact HSV values of your color. https://github.com/kyl3ru1z/HSV_ColorFinder
- On line 17 replace the HSV values. This is how you orient the values -> [hue lower, sat lower, val lower, hue max, sat max, val max].
- On line 19 replace the name of the color to match the colors that you are finding 

# What I Learned 
- Applying multiple masks
- Applying contours
- Finding HSV values 
- Putting text on a specific object

# Demo
<img src="gifs/color_detection.gif" height="400">
