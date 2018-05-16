import cv2
import numpy as np 
import sqlite3
import os
import glob

mypath = 'dataset'
conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')
c = conn.cursor()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

userid = None
try:
  try:
    userid = int(input('Enter your ID : '))
  except ValueError:
    print ("ID kosong, memasukkan data baru")
except SyntaxError:
    userid = None
uname = input("Enter your name : ")

#imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
#for f in os.listdir(mypath):
#for imagePath in imagePaths:
#  ID = imagePath
#  part = f.split('.')
  #print(part[0]+'.'+part[1])


uid = c.lastrowid
patern = "User."+str(userid)+ ".*"
#patern = "*.*"
if userid != None:
  uid = str(userid)
  os.chdir(mypath)

  filelist = glob.glob(patern)
  for f in filelist:
    os.remove(f) 
    #print(f) 
    #os.rename(f, f.replace('User.6.','User.3.'))

os.chdir(os.path.dirname(os.getcwd()))
#if userid is None:
#c.execute('INSERT INTO users (name) VALUES (?)', (uname,))
print(uid)
print(patern)
sampleNum = 0
while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    sampleNum = sampleNum+1
    print("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg")
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('img',img)
  cv2.waitKey(1);
  if sampleNum > 20: #20
    break
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()