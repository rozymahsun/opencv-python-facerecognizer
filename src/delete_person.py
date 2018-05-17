import cv2
import numpy as np 
import sqlite3
import os
import glob

mypath = 'dataset'
userid = None

try:
  userid = int(input('Masukkan ID yang akan di hapus : '))
except ValueError:
  print ("ID kosong")
patern = "User."+str(userid)+ ".*"
if userid != None:
  os.chdir(mypath)
  filelist = glob.glob(patern)
  for f in filelist:
  	print(f)
    #os.remove(f) 
