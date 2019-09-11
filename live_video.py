import cv2
import time


class live_video(object):
	
	def __init__(self):
		pass

	def record(self):
		
		video = cv2.VideoCapture(0)

		while(True):

			# get the frame (numpy array)
			ret, frame = video.read()

			cv2.imshow("pic", frame)
	
			if not ret:
				break
	
			# this will ensure we create a new frame after 1 millisecond 
			key = cv2.waitKey(1)
	
			if key == ord('q'):
				break
	
		video.release()
		cv2.destroyAllWindows()

if __name__ == '__main__':

	# Press q on the window to quit recording
	vid = live_video()		
	vid.record()
