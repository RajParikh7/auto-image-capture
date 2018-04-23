# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:16:55 2018

@author: rajpa
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#   fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
i=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        i=i+1
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        #out.write(frame)

        cv2.imshow('frame',frame)
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ri = cv2.resize(grayImg, (28, 28)) 
        ri=np.reshape(ri,[1,784]) 
        #y_=sess.run([y_],feed_dict={x_:ri})
        #y_max=np.argmax(np.array(y_))
        if i% 100 ==0:
            
            cv2.imwrite(str(i)+'.png',grayImg)
            
            #image = cv2.imread(resized_image)
            print(ri)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()