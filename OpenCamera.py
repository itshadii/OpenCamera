import cv2
import numpy as np
import os
import time

os.chdir('C:/Users/hadi_novarctech/Desktop/Test')

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FPS, 20)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture1 = cv2.VideoCapture(2)
capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture1.set(cv2.CAP_PROP_FPS, 20)
#capture2 = cv2.VideoCapture(3)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m-%d-%Y_%H-%M-%S", named_tuple)
print(time_string)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(time_string+'.mp4', vid_cod, 20.0, (1280,480))
 
while True:
    tuple1 = time.localtime() # get struct_time
    time_lapse = time.strftime("%H-%M-%S", tuple1)
    #ret if capture is working properly
    ret, frame = capture.read()
    ret, frame1 = capture1.read()
    #ret, frame2= capture2.read()
    print(time_lapse + ": Frame grapped weee")

    #Setting the frame size
    width = 2*int(capture.get(3))
    height = int(capture.get(4))
    #print("setting frame")
    #print(width, height)

    #Add Text to the frame
    frame = cv2.putText(frame, 'Camera 1', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    frame1 = cv2.putText(frame1, 'Camera 2', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    #frame2 = cv2.putText(frame2, 'Camera 3', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 5, cv2.LINE_AA)
    #print("Adding Text")
   
    #Frame.shape makes the shape of the image same as the shape of the frame of the camera
    #np.uint8 unsigned integer 8 bit 
    #Merge the two frames
    image = np.zeros((480,1280,3),np.uint8)
    image[:height, : width//2] = frame    
    image[:height,  width//2:] = frame1
    
    #image=cv2.putText(image, time_string)

    cv2.imshow('frame', image)
    #cv2.imshow('frame 2', frame2)
    output.write(image)
    if cv2.waitKey(1) == ord('q'):
        break;

capture.release()
capture1.release()
output.release()

cv2.destroyAllWindows()