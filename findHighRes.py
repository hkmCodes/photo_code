import os
import sys
import shutil
from tqdm import tqdm

#This code is assuming that u r not sorting more than 7000 photos or so
#And that u r having sufficient RAM space to store the list of photos in a map

FB_SEL = "zz_FB_SEL"

def sort(to_fldr, frm_fldr_parent, frm_fldr_child):
	
	global FB_SEL	

	#print "to folder: %s, from folder child: %s" % (to_fldr, frm_fldr_child)	
	frm_fldr = os.path.join(str(frm_fldr_parent), str(frm_fldr_child))
	#print "to folder: %s, from folder: %s" % (to_fldr, frm_fldr)	
	
	#Adding the files from frm_fldr into a set
	frmSet = set([ x[2] for x in os.walk(frm_fldr) ][-1])
	#print "frmSet: %s" % (str(frmSet))

	newValSet = set()
	#Modify values in set from .jpg to .JPG
	for val in frmSet:
		newVal = val
		newVal = newVal.replace('jpg', 'JPG')
		newValSet.add(newVal)
	del frmSet
	#print "newValSet: %s" % (str(newValSet))

	#forming the selection folder
	sel_fldr = os.path.join(to_fldr, FB_SEL)
	sel_fldr = os.path.join(sel_fldr, frm_fldr_child)

	os_walk_to_fldr = tuple(os.walk(to_fldr))
	os_walk_to_fldr = os_walk_to_fldr[:-2]
	#print "sel_fldr: %s, to_fldr: %s, frm_fldr_child: %s" % (sel_fldr, to_fldr, frm_fldr_child)
	if not os.path.exists(sel_fldr):
		os.makedirs(sel_fldr)

	#forming the directory structure
	directoryMap = { x[0]:x[2] for x in os_walk_to_fldr }
	#print "directoryMap: ", directoryMap

	#Going through each of the subdirectories in the list and getting the files you want
	for k in directoryMap:
		v = directoryMap[k]
		#print "key: %s, value: %s" % (k, v)
        	print "-------------------------------------------------------------------------------------------------------------"
        	print "                              DIR: %s                                                                    "%(k)
		print "-------------------------------------------------------------------------------------------------------------"
		for i, file in enumerate(tqdm(v)):
			origFile = os.path.join(k,file)
			if file in newValSet:
				#print "Copying - origFile: %s, sel_fldr: %s" %(origFile, sel_fldr)
				shutil.copy2(origFile, sel_fldr)				

def main():

	#call sort() with
	#frm_fldr = folder with low res photos
	#to_fldr  = folder with high res all photos

	frm_fldr_parent = "/Users/shashwath/Desktop/SORT"
	frm_fldr_children = [ x[1] for x in os.walk(frm_fldr_parent) ][0]
	#print "frm_fldr_children: %s" % (str(frm_fldr_children))
	for frm_fldr_child in frm_fldr_children:
		sort(sys.argv[1], frm_fldr_parent, frm_fldr_child)

if __name__=="__main__":
	main()
