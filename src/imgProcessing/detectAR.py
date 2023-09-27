"""
https://shuzo-kino.hateblo.jp/entry/2023/01/23/235508 フルスクリーンにする方法
https://python-academia.com/opencv-aruco/
"""

import cv2
from cv2 import aruco
import time
import numpy as np

### --- aruco設定 --- ###
dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()
main_id = 0
corner_array = []
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        frame_markers = cv2.resize(frame_markers,None,fx = 1.5, fy = 1.5)
        # 指定したラベルIDがあるか確認
        if main_id in np.ravel(ids):
            """cv2.putText(frame_markers,text = 'sample text',org = (100, 100),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 255, 0),thickness=2,lineType=cv2.LINE_4)"""
            index = np.where(ids == main_id)[0][0]
            cornerUL = corners[index][0][0]
            cornerUR = corners[index][0][1]
            cornerBR = corners[index][0][2]
            cornerBL = corners[index][0][3]
            center = [ (cornerUL[0]+cornerBR[0])/2 , (cornerUL[1]+cornerBR[1])/2 ]
            """cv2.putText(frame_markers,text = 'Uppper left : {}'.format(cornerUL),org = (20, 20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(255, 255, 255),thickness=2,lineType=cv2.LINE_4)
            cv2.putText(frame_markers,text = 'Uppper right : {}'.format(cornerUR),org = (20, 40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(250, 255, 255),thickness=2,lineType=cv2.LINE_4)
            cv2.putText(frame_markers,text = 'Bottom right : {}'.format(cornerBR),org = (20, 60),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(255, 255, 255),thickness=2,lineType=cv2.LINE_4)
            cv2.putText(frame_markers,text = 'Bottom left : {}'.format(cornerBL),org = (20, 80),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(255, 255, 255),thickness=2,lineType=cv2.LINE_4)"""
            # cv2.putText(frame_markers,text = 'Center : {}'.format(center),org = (20, 20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6,color=(255, 255, 255),thickness=2,lineType=cv2.LINE_4)
        for sub_id in range(1,5):
            if sub_id in np.ravel(ids):
                index = np.where(ids == sub_id)[0][0]
                cornerUL = corners[index][0][0]
                corner_array.append(cornerUL)
        # cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('frame', frame_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow('frame')
    cap.release()
except KeyboardInterrupt:
    cv2.destroyWindow('frame')
    cap.release()
