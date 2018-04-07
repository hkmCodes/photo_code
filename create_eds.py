import os
import sys
import shutil

V_FLDR = 'v'

def create_eds(fldr):
	
	#Getting immediate subdirectories of fldr
	dirList = next(os.walk(fldr))[1]
	print 'fldr: %s, dirList: %s' % (fldr, dirList)

	#The new ed dirs required
	eds = ['ed', 'ed_wm', 'ed_wm_fb']

	#Going through each immediate subdirectories and creating ed folders there
	for dir in dirList:
		subdir = os.path.join(fldr, dir)
		for ed in eds:
			subed = os.path.join(subdir, ed)
			if not os.path.exists(subed):
				print "Creating subed: %s" % (subed)
				os.makedirs(subed)
			if ed == 'ed_wm_fb':
				ed_fb_v = os.path.join(subed, V_FLDR)
				if not os.path.exists(ed_fb_v):
					os.makedirs(ed_fb_v)

def main():
	fldr = sys.argv[1]
	create_eds(fldr)

if __name__ == "__main__":
	main()
				
