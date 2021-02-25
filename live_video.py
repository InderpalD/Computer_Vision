import cv2
import time

class Live_Video(object):
	''' Uses webcam to start a live video '''
	
	def __init__(self):
		'''constructor'''
		pass

	def record(self):
		''' Start recording using your camera feed '''
		video = cv2.VideoCapture(0)
		while(True):

			# get the frame (numpy array)
			ret, frame = video.read()
			cv2.imshow("pic", frame)
	
			if not ret:
				break
	
			# this will ensure we create a new frame
			key = cv2.waitKey(1)
	
			if key == ord('q'):
				break
	
		video.release()
		cv2.destroyAllWindows()

if __name__ == '__main__':

	# Press q on the window to quit recording
	vid = Live_Video()		
	vid.record()
