import cv2 
import cv2.aruco as aruco
import numpy as np
path8 = "2.jpg"
path9 = "CVtask.jpg"
path10 = "1.jpg"
path11 = "3.jpg"
path12 = "4.jpg"
image2 = cv2.imread(path8)
image3 = cv2.imread(path9)
image4 = cv2.imread(path10)
image5 = cv2.imread(path11)
image6 = cv2.imread(path12)
resized_image2 = cv2.resize(image2,(400,400))
resized_image3 = cv2.resize(image3,(400,400))
resized_image4 = cv2.resize(image4,(400,400))
resized_image5 = cv2.resize(image5,(400,400))
resized_image6 = cv2.resize(image6,(400,400))
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
 
# driver function
if __name__=="__main__":
 
    # reading the image
    img = cv2.imread(path8, 1)
    resized_img = cv2.resize(img,(400,400))
 
    # displaying the image
    cv2.imshow('image', resized_img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()

def imageaugmentation(img,imgAug2,imgAug1,imgAug3,imgAug4):
    pts1 = np.array([[266,24],[349,24],[349,140],[266,140]])
    pts0 = np.array([[46,12],[137,42],[115,172],[23,141]])
    ptsa = np.array([[321,154],[382,189],[357,279],[295,242]])
    ptsb = np.array([[75,217],[182,135],[241,287],[135,366]])
    pts2 = np.array([[82,14],[391,83],[320,392],[11,321]])
    pts3 = np.array([[31,109],[304,32],[381,304],[110,379]])
    pts4 = np.array([[53,52],[350,52],[350,349],[53,349]])
    pts5 = np.array([[18,97],[305,17],[383,305],[96,382]])
    matrix4,_ = cv2.findHomography(pts5,ptsb)
    matrix3,_ = cv2.findHomography(pts4,ptsa)
    matrix2,_ = cv2.findHomography(pts3,pts0)
    matrix,_ = cv2.findHomography(pts2,pts1)
    imgout4 = cv2.warpPerspective(imgAug4,matrix4,(img.shape[1],img.shape[0]))
    imgout3 = cv2.warpPerspective(imgAug3,matrix3,(img.shape[1],img.shape[0]))
    imgout2 = cv2.warpPerspective(imgAug1,matrix2,(img.shape[1],img.shape[0]))
    imgout = cv2.warpPerspective(imgAug2,matrix,(img.shape[1],img.shape[0]))
    cv2.fillConvexPoly(img,pts0.astype(int),(0,0,0))
    cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
    cv2.fillConvexPoly(img,ptsa.astype(int),(0,0,0))
    cv2.fillConvexPoly(img,ptsb.astype(int),(0,0,0))
    

    return cv2.imshow('imgout',img+imgout+imgout2+imgout3+imgout4)

imageaugmentation(resized_image3,resized_image2,resized_image4,resized_image5,resized_image6)



def findAruco(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_5X5_50')
    arucodict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    (corners,ids,rejected) = cv2.aruco.detectMarkers(gray,arucodict,parameters=arucoParam)
    print(ids)
    if len(corners) > 0:
        ids =ids.flatten()

        for(markerCorner,markerID) in zip(corners,ids):
            
            corners = markerCorner.reshape((4,2))
            (topLeft,topRight,bottomRight,bottomLeft) = corners

            topLeft = (int(topLeft[0]),int(topLeft[1]))
            topRight = (int(topRight[0]),int(topRight[1]))
            bottomRight = (int(bottomRight[0]),int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]),int(bottomLeft[1]))

            cx = int((topLeft[0]+bottomRight[0])/2.0)
            cy = int((topLeft[1]+bottomRight[1])/2.0)

            cv2.circle(img,(cx,cy),5,(255,0,0),-1)
            cv2.putText(gray,str(markerID),(cx,cy-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),cv2.LINE_AA)

findAruco(image2)
findAruco(image4)
findAruco(image5)
findAruco(image6)


