import cv2
import numpy as np

matrix_coefficient = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
distortion_coefficient = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

# position estimation function
def pos_estimation(frame,matrix_coefficient,distortion_coefficient):
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Change grayscale
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(gray, arucoDict,
        parameters=arucoParams)
    if np.all(ids is not None):
        for i in range(0, len(ids)):
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficient,
                                                                       distortion_coefficient)
            (rvec - tvec).any()  # get rid of that nasty numpy value array error
            cv2.aruco.drawDetectedMarkers(frame, corners)  # Draw A square around the markers
            # cv2.aruco.drawAxis(frame, matrix_coefficient, distortion_coefficient, rvec, tvec, 0.01)  # Draw Axis
            
        cv2.imshow("Detected Markers", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No markers found")
       

frame = cv2.imread("image.jpg")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# binary threshold
ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
#frame = cv2.imread("tag2.png")
pos_estimation(thresh,matrix_coefficient,distortion_coefficient)
