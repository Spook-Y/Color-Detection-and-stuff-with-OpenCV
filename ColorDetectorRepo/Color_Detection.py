import cv2
import numpy as np

#This was made by Yan R. - Spook-Y
#Code that I might use later to improve the program.
        ##Create bilateral image##
        #bilateral_image = cv2.bilateralFilter(self.picture, 5, 175, 175)
        ##Detect edges##
        #edgy_image = cv2.Canny(bilateral_image, 75, 200)
        #Create a contour list.

class ColorDetector(object):

    #Initializer. Creates an instance of the object.
    def __init__(self, picture, upper, lower, mask,markingColor):
        super(ColorDetector, self).__init__()
        self.picture = picture
        self.upper = upper
        self.lower = lower
        self.mask = mask
        self.markingColor = markingColor

    #Sets the image variable, the one used to actually detect the color.
    def set_image(self,picture):
        self.picture = cv2.imread(picture)

    #Sets the upper 3 dimensional array of the color detector object.
    def set_upper(self,l):
        self.upper = np.array(l)

    #Sets the lower 3 dimensional array of the color detector object.
    def set_lower(self, l):
        self.lower = np.array(l)

    #Sets the color in which the items will be marked. Default is black.
    def set_marking_color(self,marking):
        self.markingColor = marking

    #returns the upper array of the current color detector object.
    def get_upper(self):
        return self.upper

    #returns the lower array of the current color detector object.
    def get_lower(self):
        return self.lower

    #returns the value within marking color.
    def get_marking_color(self):
        return self.markingColor

    #Creates the mask that will be used to show the picture.
    def create_mask(self):
        #Attempts at optimization that are scratched temporarily.
        ##Create bilateral image##
        #bilateral_image = cv2.bilateralFilter(self.picture, 5, 175, 175)
        ##Detect edges##
        #edgy_image = cv2.Canny(bilateral_image, 75, 200)
        self.mask = cv2.inRange(self.picture, self.lower, self.upper)

    #returns the mask of the current color detector object.
    def get_mask(self):
        return self.mask

    #Creates the contour of the maked image and displays the image with a box drawn around whatever object is in said
    #color.
    def find_item_in_picture(self, mask, picture):
        try:
        #Create a list that will contain the contours.
            contour_list = []

        #Find the contour in the masked image and keep the largest one.
            (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_TREE,
        	   cv2.CHAIN_APPROX_SIMPLE)
            c = max(cnts, key=cv2.contourArea)

        #Approximate the contour.
            peri = cv2.arcLength(c, True)
            for contour in cnts:
                approx = cv2.approxPolyDP(contour, 0.01 * peri, True)
                area = cv2.contourArea(contour)
                if(len(approx) > 8 & (area < 30)):
                    contour_list.append(contour)

        #Draw mark around detected image color.
            cv2.drawContours(picture, contour_list, -1, self.markingColor, 2)
        except:
            pass

    #Returns boolean value stating if the color is found in the picture.
    def is_color_there(self):
        if(cv2.countNonZero(self.mask) > 0):
            return True
        else:
            return False
