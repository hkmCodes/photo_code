import os
import sys
import shutil
from tqdm import tqdm

PHOTO_EXT  = ('.JPG', '.PNG')
VIDEO_EXT  = ('.MOV', '.MP4')
PHOTO_EXT2 = ()
VIDEO_EXT2 = ()
PHOTOS     = 'Photos'
VIDEOS     = 'Videos'

def sort_photo_video(masterPath):
	global PHOTO_EXT, VIDEO_EXT, PHOTO_EXT2, VIDEO_EXT2, PHOTOS, VIDEOS
	masterPathLen  = len(masterPath)
	masterPathWalk = []
	masterPathPhotoDirs = []
	masterPathVideoDirs = []

	for x in os.walk(masterPath):
		masterPathWalk.append(x)
	
	#Creating photo and video directory paths
	for x in masterPathWalk:
		newPhotoPath = os.path.join(masterPath, PHOTOS, x[0][masterPathLen+1:])
		masterPathPhotoDirs.append(newPhotoPath)
		if not os.path.exists(newPhotoPath):
			os.makedirs(newPhotoPath)
		
		newVideoPath = os.path.join(masterPath, VIDEOS, x[0][masterPathLen+1:])
		masterPathVideoDirs.append(newVideoPath)
		if not os.path.exists(newVideoPath):
			os.makedirs(newVideoPath)

	#print "----------------------------------------------------------------------------------"
	#print "masterPathPhotoDirs: ", masterPathPhotoDirs
	#print "masterPathVideoDirs: ", masterPathVideoDirs
	#print "----------------------------------------------------------------------------------"
	#TODO: get list of files and the run tqdm on that

	print "----------------------------------------------------------------------------------"
	print "                            PHOTOS TRANSFER                                       "
	print "----------------------------------------------------------------------------------"
	#Transfering the files to Photo and Video folders
	for i, x in enumerate(tqdm(masterPathWalk)):
		#print "Transferring photos in directory: ", x[0]
		for f in x[2]:
			if f.endswith(PHOTO_EXT) or f.endswith(PHOTO_EXT2):
				shutil.copy(os.path.join(x[0], f), masterPathPhotoDirs[i])

	print "----------------------------------------------------------------------------------"
	print "                            VIDEOS TRANSFER                                       "
	print "----------------------------------------------------------------------------------"
	for i, x in enumerate(tqdm(masterPathWalk)):
		#print "Transferring videos in directory: ", x[0]
		for f in x[2]:
			if f.endswith(VIDEO_EXT) or f.endswith(VIDEO_EXT2):
				shutil.copy(os.path.join(x[0], f), masterPathVideoDirs[i])

def main():
	global PHOTO_EXT2, VIDEO_EXT2
	PHOTO_EXT2 = tuple(x.lower() for x in PHOTO_EXT)
	VIDEO_EXT2 = tuple(x.lower() for x in VIDEO_EXT)	
	sort_photo_video(sys.argv[1])

if __name__=="__main__":
	main()
