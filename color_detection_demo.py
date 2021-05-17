import cv2
import numpy as np

# second property fixes a bug
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Frame Width
cap.set(3, 640)
# Frame Height
cap.set(4, 480)
# adjusting brightness
cap.set(10, 140)

# HSV stands for Hue Saturation and Value (The V in HSV is also known as brightness).
# array of lower and upper hsv values - [hue lower, sat lower, val lower, hue max, sat max, val max]
# we want to take the lower and upper values and extract the colors in between to get the colors
# HSV is used because unlike RGB, HSV separates luma, or the image intensity, from chroma or the color information
myColors = [[0, 137, 121, 19, 255, 255], [52, 65, 119, 138, 255, 255], [120, 65, 77, 132, 224, 178]]
# names for the colors of the above values
colorName = ["Orange", "Green", "Purple"]

def findColor(cap, myColors):
    # the reason why the HSV looks a bit odd because we are trying to display our HSV colored image as a BGR image so the pixels are being read in a weird fashion.
    capHSV = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        # numpy arrays are used because that is what is needed to be passed in by OpenCV
        # here i am looping through my upper and lower hsv.
        lower = np.array([color[0:3]])
        upper = np.array([color[3:6]])
        # applying my upper and lower hsv values into a mask
        mask = cv2.inRange(capHSV, lower, upper)
        #passing that mask into my get contours function.
        #if a color matches my mask than the x and y values of my names will get updates on top of the color
        #if a color is not certain color is not detected the x and y values will stay off screen where they were initialized
        x, y = getContours(mask)
        cv2.putText(videoResult, colorName[count], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        count += 1

def getContours(cap):
    # second property is a retrieval method and it retrieves the extreme outer contours.
    # third property is a takes in an approximation method that can  give you all of the information or compressed values
    # once we have contours it will be saves in the contours variable.
    contours, hierarchy = cv2.findContours(cap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # i am initializing the x and y off screen because if a color isn't detected we wouldn't want the name of the color on the screen
    x, y, w, h = -30, -30, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Defining a minimum threshold for our area so it does not catch any noise.
        if area > 500:
            cv2.drawContours(videoResult, cnt, -1, (0, 255, 0), 1)
            # finds the perimeter of a contour
            perimeter = cv2.arcLength(cnt, True)
            # It approximates a contour shape to another shape
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            # uses that approximation to draw a rectangle around our item
            x, y, w, h = cv2.boundingRect(approx)
    # we are returning an x and y value that is approximately at the center of the rectangle
    return x-w//2, y


while True:
    # the reason why there are two variables here is because cap.read() returns a boolean and image content
    sucess, video = cap.read()
    # mirroring our image
    videoFlip = cv2.flip(video, 1)
    # we have to copy the image we are passing in, if we do not it will cause an error.
    videoResult = videoFlip.copy()
    findColor(videoResult, myColors)
    cv2.imshow("Color Detection Demo", videoResult)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
