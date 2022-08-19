import cv2
import os


os.chdir("C:/Users/hadi_novarctech/Desktop/Test")
cap= cv2.VideoCapture(1)
cap1= cv2.VideoCapture(0)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width1= int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1= int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'.mp4'), 30, (width,height))
writer1= cv2.VideoWriter('secondvideo.mp4', cv2.VideoWriter_fourcc(*'.mp4'), 30, (width1, height1))


while True:
    ret,frame= cap.read()
    ret,frame1= cap1.read()
    #Change color to greyscale	
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)
     
 
    writer.write(grayFrame)
    writer.write(frame1)
    cv2.imshow('video original', frame1)
    cv2.imshow('frame', grayFrame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
writer.release()
cv2.destroyAllWindows()


