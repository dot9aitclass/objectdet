import numpy as np
import cv2
area=[]
avarea=[]
kernel = np.ones((5,5),np.uint8)
cap=cv2.VideoCapture(0)
ret,im=cap.read()
ex=0
why=0
test=(0,0)
# cv2.imshow("size",im)
# cv2.waitKey()
# cv2.destroyAllWindows()
def coordinates(event,x,y,flags,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        global ex
        global why
        ex=x
        why=y
        print ("x=",x,"y=",y)
u=116
v=87
lower_color = np.array([0,u-30,v-30])
upper_color = np.array([255,u+30,v+30])
while True:

        # Take each frame
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        thresh=cv2.Canny(res,100,200)
        contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(thresh, contours1, -1 , (0,0,255), 3)
        for i in range(len(contours1)):
                area.append(cv2.contourArea(contours1[i]))
        (m,n),radius = cv2.minEnclosingCircle(contours1[0])
        center = (int(m),int(n))
        r = int(radius)
        for i in range(len(contours1)):
                #avarea.append(cv2.contourArea(contours1[i]))
                (m,n),radius = cv2.minEnclosingCircle(contours1[i])
                if radius > r:
                        center = (int(m),int(n))
                        r = int(radius)
                        ind = i
        (m,n),radius= cv2.minEnclosingCircle(contours1[ind])
        center=(int(m),int(n))
        if test!=center:
                cv2.circle(frame,center,int(radius),(0,255,0),2)
                
        test=center
        cv2.imshow("im3",frame)
        cv2.setMouseCallback('im3',coordinates)
        val=cv2.waitKey(1)
        if val==27:
                print ("x=",center[0],"y=",center[1])
                print ("x=",round((center[0]-320)*(0.0854)),"y=",round((480-center[1])*(0.0854)))
                #break
        elif val==ord('c'):
                break #print ("x=",center[0],"y=",center[1])
                #print ("x=",round((center[0]-320)*(30/357))-4,"y=",round((480-center[1])*(30/357))-9)


# print ("x=",center[0],"y=",center[1])
# print ("x=",round((center[0]-320)*(30/357))-4,"y=",round((480-center[1])*(30/357))-9)
# print ("to"+"\n","x=",ex,"y=",why)
# print ("x=",(ex-320)*(30/357)-4,"y=",(480-why)*(30/357)-9)

        #cv2.imshow('frame',frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res',res)
        #if cv2.waitKey(30)==27:
        #break
# thresh=cv2.Canny(res,100,200)
# im3, contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(thresh, contours1, -1 , (0,0,255), 3)
# for i in range(len(contours1)):
#         area.append(cv2.contourArea(contours1[i]))
# (m,n),radius = cv2.minEnclosingCircle(contours1[0])
# center = (int(m),int(n))
# r = int(radius)
# for i in range(len(contours1)):
#         avarea.append(cv2.contourArea(contours1[i]))
#         (m,n),radius = cv2.minEnclosingCircle(contours1[i])
#         if radius > r:
#                 center = (int(m),int(n))
#                 r = int(radius)
#                 ind = i
"""(x,y),radius = cv2.minEnclosingCircle(contours1[ind])
center = (int(x),int(y))
radius = int(radius)"""
# cv2.circle(im,center,radius,(0,255,0),2)
# print center[0],center[1]
# ret1,im=cap.read()
# (m,n),radius= cv2.minEnclosingCircle(contours1[ind])
# center=(int(m),int(n))
# #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.circle(im,center,int(radius),(0,255,0),2)
# # cv2.imshow("im3",im)
# # cv2.waitKey()
# print (center)
# print ("x=",center[0]-320)
# print ("y=",480-center[1])
# """rect = cv2.minAreaRect(contours[ind])
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# print box"""
# #cv2.drawContours(img,[box],0,(0,0,255),2)
# while True:
#         _, im = cap.read()
#         cv2.circle(im,center,int(radius),(0,255,0),2)
#         cv2.imshow("im3",im)
#         cv2.setMouseCallback('im3',coordinates)
#         if cv2.waitKey(30)==27:
#                 break
# cv2.destroyAllWindows()
# print ("x=",center[0],"y=",center[1])
# print ("to"+"\n","x=",ex,"y=",why)
# """
# cv2.imshow("ed",thresh)
# k=cv2.waitKey()


# maxval=max(area)


# print len(area)
# print ind
# cv2.drawContours(im, contours, -1 , (0,0,255), 3)

# print x,y

# cv2.imshow("im",im)
# k=cv2.waitKey()"""
# """thresh=cv2.Canny(thresh,100,200)
# im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for i in range(len(contours)):
#         area.append(cv2.contourArea(contours[i]))
# (x,y),radius = cv2.minEnclosingCircle(contours[0])
# center = (int(x),int(y))
# r = int(radius)
# #cv2.drawContours(im, contours, -1 , (0,0,255), 3)
# for i in range(len(contours)):
#         avarea.append(cv2.contourArea(contours[i]))
#         (x,y),radius = cv2.minEnclosingCircle(contours[i])
#         if radius > r:
#                 center = (int(x),int(y))
#                 r = int(radius)
#                 ind = i
# (x,y),radius = cv2.minEnclosingCircle(contours[ind])
# center = (int(x),int(y))
# radius = int(radius)
# cv2.circle(im,center,radius,(0,255,0),2)
# f=center[0]
# s=center[1]
# color=im[s][f]
# cv2.imshow("frame",im)
# if cv2.waitKey(30)==27:
#         break"""
#129,116,87​
"""print np.size(im,0),np.size(im,1)
imgray = im #cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imgray = cv2.morphologyEx(imgray, cv2.MORPH_CLOSE, kernel)
imgray = cv2.morphologyEx(imgray, cv2.MORPH_CLOSE, kernel)
imgray = cv2.morphologyEx(imgray, cv2.MORPH_CLOSE, kernel)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
imgray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
imgray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
imgray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
imgray = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
thresh=cv2.Canny(imgray,100,200)
# blur = cv2.GaussianBlur(imgray,(5,5),0)
# ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("frame",thresh)
cv2.waitKey()
cv2.destroyAllWindows()
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
        area.append(cv2.contourArea(contours[i]))
(x,y),radius = cv2.minEnclosingCircle(contours[0])
center = (int(x),int(y))
r = int(radius)
#cv2.drawContours(im, contours, -1 , (0,0,255), 3)
for i in range(len(contours)):
        avarea.append(cv2.contourArea(contours[i]))
        (x,y),radius = cv2.minEnclosingCircle(contours[i])
        if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
(x,y),radius = cv2.minEnclosingCircle(contours[ind])
center = (int(x),int(y))
radius = int(radius)
#cv2.circle(im,center,radius,(0,255,0),2)
f=center[0]
s=center[1]
color=im[s][f]
cv2.imshow("frame",im)
cv2.destroyAllWindows()
print color
chsv=np.uint8([[color]])
colorhsv=cv2.cvtColor(chsv,cv2.COLOR_BGR2HSV)
colorhsv=colorhsv[0][0]
print colorhsv"""
