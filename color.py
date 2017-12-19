from transferColor.transCOLOR import trans_color
import numpy as np
import argparse
import cv2

def show_image(title, image, width =700):
	# resize to constant width
	r = width / float(image.shape[1])
	#maintain aspect ratio
	dim = (width, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	# show the resized image
	cv2.imshow(title, resized)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,
	help = "Path to the source image")
ap.add_argument("-t", "--target", required = True,
	help = "Path to the target image")
args = vars(ap.parse_args())

# load the images
source = cv2.imread(args["source"])
target = cv2.imread(args["target"])

# transfer color distribution from the source image
# to the target image
transfer = trans_color(source, target)

# save image
cv2.imwrite("transfer.png", transfer)

# show the images and wait for a key press
show_image("Source", source)
show_image("Target", target)
show_image("Transfer", transfer)
cv2.waitKey(0)