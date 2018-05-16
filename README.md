# opencv-python-facerecognizer
An openCV and Python Face Recognizer

Face recognition with opencv and python
==========================================

How does it work?
-------------------

1. Record a faces to database
2. Train dataset
3. Detect a face

Requirement
-------------------

* [Python](http://www.python.org)
* [SQLite](http://www.sqlite.org/)
* [OpenCV](http://opencv.org) with python bindings (I'm using the trunk version)
* [PIL](http://www.pythonware.com/products/pil/)

>pip freeze
* numpy==1.14.3
* opencv-contrib-python==3.4.0.12
* Pillow==5.1.0

Runnning it
-------------------
- Activate virtual environtment 
- goto "./src/" folder 

1. >python create-database.py
   create a python database tables
   
2. >python record-face.py
   record a face, and put image to "./src/dataset/" folder with pattern "User.[user.id].[pic.number].jpg"

3. >python trainer.py
   train dataset and generate training data to "./src/recognizer/trainingData.yml"

4. >python detector.py
   detect a face 
