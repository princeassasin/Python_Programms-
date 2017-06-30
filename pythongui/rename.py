#!/usr/bin/env python

""" This is python script by Sriram Sountharapandian Mathivanan to automate a script by renaming a bunch of files using python 2.7 version """


import os

os.chdir('/home/sriram/script2/photo2')

#print(os.getcwd())

for f in os.listdir('/home/sriram/script2/photo2'):
	f_name, f_ext =os.path.splitext(f)
	f_title, f_num = f_name.split('_',1)
	
	#f_title = f_title.strip()
	#f_num = f_num.strip()
	new_name = '{}_{}{}'.format(f_num, f_title, f_ext)

	os.rename(f, new_name)	
