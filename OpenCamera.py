import cv2
import numpy as np
import os
import time

os.chdir('C:/Users/hadi/Desktop/Test')

capture = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m-%d-%Y-%H-%M-%S", named_tuple)
print(time_string)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(time_string+'.mp4', vid_cod, 20.0, (1280,480))

while True:
    #ret if capture is working properly
    ret, frame = capture.read()
    ret, frame1 = capture1.read()

    #Setting the frame size
    width = 2*int(capture.get(3))
    height = int(capture.get(4))

    #Add Text to the frame
    frame = cv2.putText(frame, 'Camera 1', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 5, cv2.LINE_AA)
    frame1 = cv2.putText(frame1, 'Camera 2', (200, height -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 5, cv2.LINE_AA)

   
    #Frame.shape makes the shape of the image same as the shape of the frame of the camera
    #np.uint8 unsigned integer 8 bit 
    #Merge the two frames
    image = np.zeros((480,1280,3),np.uint8)
    image[:height, : width//2] = frame    
    image[:height,  width//2:] = frame1
    #image=cv2.putText(image, time_string)

    cv2.imshow('frame', image)
    output.write(image)
    if cv2.waitKey(1) == ord('q'):
        break;

capture.release()
capture1.release()
output.release()

cv2.destroyAllWindows()
