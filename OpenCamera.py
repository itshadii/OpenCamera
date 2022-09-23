import cv2
import numpy as np
import os
import time

os.chdir('C:/Users/hadi/Desktop/Test') 

File_name= input("Enter File Name: ")


capture = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)
capture2 = cv2.VideoCapture(2)

capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
capture1.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.50)
capture2.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)



vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(File_name+'.mp4', vid_cod, 20.0, (1280,960))

while True:
    #ret if capture is working properly
    ret, frame = capture.read()
    ret, frame1 = capture1.read()
    ret, frame2 = capture2.read()

    #Setting the frame size
    width = 2*int(capture.get(3))
    height = 2*int(capture.get(4))

    #Add Text to the frame
    frame = cv2.putText(frame, 'Camera 1', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 5, cv2.LINE_AA)
    frame1 = cv2.putText(frame1, 'Camera 2', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 5, cv2.LINE_AA)

   
    #Frame.shape makes the shape of the image same as the shape of the frame of the camera
    #np.uint8 unsigned integer 8 bit 
    #Merge the two frames
    image = np.zeros((height,width,3),np.uint8)
    image[:height//2, : width//2] = frame    
    image[:height//2,  width//2:] = frame1
    image[height//2:,  :width//2] = frame2

    #image=cv2.putText(image, time_string)

    cv2.imshow('frame', image)
    output.write(image)
    if cv2.waitKey(1) == ord('q'):
        break;

capture.release()
capture1.release()
output.release()

cv2.destroyAllWindows()