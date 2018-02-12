import cv2
import argparse
import numpy as np
import Color_Detection

#Initializing the object instances.
colorDetectorRed = Color_Detection.ColorDetector("", [], [], "",())
colorDetectorGreen = Color_Detection.ColorDetector("", [], [], "",())
colorDetectorPurple = Color_Detection.ColorDetector("", [], [], "",())
colorDetectorYellow = Color_Detection.ColorDetector("", [], [], "",())
colorDetectorOrange = Color_Detection.ColorDetector("", [], [], "",())

def main():
    #Parses command line argument for image file string.
    parser = argparse.ArgumentParser(description="Detects pre-defined colors within an image.")
    parser.add_argument('-i', action='store', dest = 'image', help = "Detect colors within image.")

    results = parser.parse_args()
    image = results.image
    picture = cv2.imread(image)

    #Set up red color detector
    colorDetectorRed.set_upper([0, 0, 255])
    colorDetectorRed.set_lower([0, 0, 10])
    colorDetectorRed.set_image(image)

    #Set up green color detector
    colorDetectorGreen.set_upper([0, 255, 0])
    colorDetectorGreen.set_lower([0, 10, 0])
    colorDetectorGreen.set_image(image)
    colorDetectorGreen.set_marking_color((0,0,255))

    #Set up orange color detector
    colorDetectorOrange.set_upper([51, 153, 255])
    colorDetectorOrange.set_lower([0, 102, 204])
    colorDetectorOrange.set_image(image)
    colorDetectorOrange.set_marking_color((255,0,0))

    #Set up yellow color detector
    colorDetectorYellow.set_upper([102, 255, 255])
    colorDetectorYellow.set_lower([0, 255, 255])
    colorDetectorYellow.set_image(image)
    colorDetectorYellow.set_marking_color((0,255,0))

    #Set up purple color detector
    colorDetectorPurple.set_upper([102, 0, 204])
    colorDetectorPurple.set_lower([51, 0, 25])
    colorDetectorPurple.set_image(image)
    colorDetectorPurple.set_marking_color((0,255,255))

    #Create masks
    colorDetectorRed.create_mask()
    colorDetectorGreen.create_mask()
    colorDetectorOrange.create_mask()
    colorDetectorYellow.create_mask()
    colorDetectorPurple.create_mask()

    #Finds items with that color in the picture
    colorDetectorRed.find_item_in_picture(colorDetectorRed.mask, picture)
    colorDetectorGreen.find_item_in_picture(colorDetectorGreen.mask, picture)
    colorDetectorOrange.find_item_in_picture(colorDetectorOrange.mask, picture)
    colorDetectorYellow.find_item_in_picture(colorDetectorYellow.mask, picture)
    colorDetectorPurple.find_item_in_picture(colorDetectorPurple.mask, picture)

    #Determines whether there is an item of that color in the picture.
    print "Red: " + str(colorDetectorRed.is_color_there())
    print "Green: " + str(colorDetectorGreen.is_color_there())
    print "Orange: " + str(colorDetectorOrange.is_color_there())
    print "Yellow: " + str(colorDetectorYellow.is_color_there())
    print "Purple: " + str(colorDetectorPurple.is_color_there())

    #Shows image with masks applied.
    cv2.imshow("Detected items in picture", picture)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
