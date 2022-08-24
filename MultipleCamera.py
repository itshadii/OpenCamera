from threading import Thread
import cv2, time
import os 


os.chdir('C:/Users/hadi/Desktop/Test')


 
class VideoStreamWidget(object):
    def __init__(self, src):
        self.capture = cv2.VideoCapture(src)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)
    
    def show_frame(self):
        # Display frames in main program
        cv2.imshow('frame', self.frame)
        if cv2.waitKey(1) == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            

if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget(0)
    video_stream_widget1 = VideoStreamWidget(1)
    while True:
            try:
                video_stream_widget.show_frame()
                video_stream_widget1.show_frame()
            except AttributeError:
                pass