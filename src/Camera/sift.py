#https://docs.opencv.org/4.x/da/de9/tutorial_py_epipolar_geometry.html

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#-------------------------------------------------------------
def drawlines(img1, img2, lines, pts1, pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c = img1.shape
    img1 = cv.cvtColor(img1,cv.COLOR_GRAY2BGR)
    img2 = cv.cvtColor(img2,cv.COLOR_GRAY2BGR)
    for r,pt1,pt2 in zip(lines,pts1,pts2):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        img1 = cv.line(img1, (x0,y0), (x1,y1), color,1)
        img1 = cv.circle(img1,tuple(pt1),5,color,-1)
        img2 = cv.circle(img2,tuple(pt2),5,color,-1)
    return img1,img2
#end-def

#-------------------------------------------------------------
cameraImage1 = "myImage.png"
cameraImage2 = "myImage.png"
img1 = cv.imread(cameraImage1, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(cameraImage2, cv.IMREAD_GRAYSCALE)

#-------------------------------------------------------------
sift = cv.SIFT_create()

#-------------------------------------------------------------
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

#-------------------------------------------------------------
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
#-------------------------------------------------------------
pts1, pts2 = [], []
 
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)
    #end-if-else
#end-for




#-------------------------------------------------------------
#Now we have the list of best matches from both the images. Let's find the Fundamental Matrix. 
pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
#https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga59b0d57f46f8677fb5904294a23d404a
F, mask = cv.findFundamentalMat(pts1, pts2, cv.FM_LMEDS)
print(f"Fundamental Matrix:\n{F}\n")


# We select only inlier points
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]

#-------------------------------------------------------------
# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image
lines1 = cv.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2,F)
lines1 = lines1.reshape(-1,3)
img5,img6 = drawlines(img1, img2, lines1, pts1, pts2)
 
# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2, img1, lines2, pts2, pts1)
 
plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img3)
plt.show()
#-------------------------------------------------------------



with open("cameraMatrixLeft.dat", 'rb') as fid: KL = np.load(fid)
with open("cameraMatrixRight.dat", 'rb') as fid: KR = np.load(fid)
E = KL.T * F * KR
print(f"Essential Matrix:\n{E}\n")

#-------------------------------------------------------------
#Decompose the Essential Matrix
#https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html#ga54a2f5b3f8aeaf6c76d4a31dece85d5d
R1, R2, t = cv.decomposeEssentialMat(E)
print(f"Rotation Matrix Nr.1:\n{R1}")
print(f"Rotation Matrix Nr.2:\n{R2}\n")
print(f"Translation Vector:\n{t}\n")

#-------------------------------------------------------------
with open("fundamentalMatrix.dat", "+wb") as fid: np.save(fid, F)
with open("essentialMatrix.dat"  , "+wb") as fid: np.save(fid, E)
with open("rotationMatrix1.dat"  , "+wb") as fid: np.save(fid, R1)
with open("rotationMatrix2.dat"  , "+wb") as fid: np.save(fid, R2)
with open("translationVector.dat", "+wb") as fid: np.save(fid, t)
#-------------------------------------------------------------

input(">>>")