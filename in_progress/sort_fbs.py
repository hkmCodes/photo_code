from PIL import Image
import os
import sys
import shutil

V_FLDR = "v"

def sortHV(fldr):
	
	#Get images at given folder
	images = next(os.walk(fldr))[2]
	print "images: %s" % (str(images))

	#create v folder
	vFldr = os.path.join(fldr, V_FLDR)
	if not os.path.exists(vFldr):
		os.makedirs(vFldr)

	for img_file_name in images:
		img_file = os.path.join(fldr, img_file_name)
		img = Image.open(img_file)
		width, height = img.size
		print "img: %s, w_h %s" % (img_file_name, (width, height))
		print "img_file: %s" % (img_file)
		if height > width:
			shutil.copy(img_file, vFldr)

def main():
	fldr = sys.argv[1]
	sortHV(fldr)

if __name__ == "__main__":
	main()
